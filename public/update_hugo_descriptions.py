import csv
import os
import re
from pathlib import Path

def update_markdown_files(csv_path, content_dir):
    # Step 1: Load and normalize CSV slugs
    slug_descriptions = {}
    with open(csv_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Normalize slug by removing leading/trailing slashes and spaces
            clean_slug = row['slug'].strip('/').strip()
            slug_descriptions[clean_slug] = row['yoast_metadescription']
    
    print(f"Loaded {len(slug_descriptions)} slugs from CSV")

    # Step 2: Process all markdown files
    matches = []
    no_match_files = []
    total_files = 0

    for root, _, files in os.walk(content_dir):
        for filename in files:
            if filename.endswith('.md'):
                total_files += 1
                filepath = Path(root) / filename
                
                with open(filepath, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Extract URL path from frontmatter
                    url_match = re.search(r'url:\s*/([^\s]+)/?', content)
                    if url_match:
                        url_slug = url_match.group(1).strip()
                        url_slug = url_match.group(1).strip("/");
                        
                        # Check for exact match with CSV slugs
                        print(url_slug);
                        print(url_slug in slug_descriptions);
                        if url_slug in slug_descriptions:
                            # Prepare the description (escape quotes)
                            description = slug_descriptions[url_slug].replace('"', '\\"')
                            
                            # Check if description already exists
                            if not re.search(r'^description:\s', content, re.MULTILINE):
                                # Insert description after first frontmatter delimiter
                                new_content = re.sub(
                                    r'^(---\n)',
                                    f'---\ndescription: "{description}"\n',
                                    content,
                                    count=1
                                )
                                
                                # Write changes back to file
                                f.seek(0)
                                f.write(new_content)
                                f.truncate()
                            
                            matches.append({
                                'file': str(filepath),
                                'slug': url_slug,
                                'description': description[:50] + '...' if len(description) > 50 else description
                            })
                        else:
                            no_match_files.append({
                                'file': str(filepath),
                                'slug': url_slug,
                                'reason': 'No matching slug in CSV'
                            })
                    else:
                        no_match_files.append({
                            'file': str(filepath),
                            'reason': 'No valid URL in frontmatter'
                        })

    # Step 3: Print detailed results
    print("\n=== MATCHED FILES ===")
    for match in matches:
        print(f"📄 File: {match['file']}")
        print(f"🔗 Slug: {match['slug']}")
        print(f"📝 Description: {match['description']}\n")

    print("\n=== UNMATCHED FILES ===")
    for no_match in no_match_files:
        print(f"📄 File: {no_match['file']}")
        if 'slug' in no_match:
            print(f"🔗 Slug: {no_match['slug']}")
        print(f"❌ Reason: {no_match['reason']}\n")

    print("\n=== SUMMARY ===")
    print(f"Total files processed: {total_files}")
    print(f"Successfully matched: {len(matches)}")
    print(f"Unmatched files: {len(no_match_files)}")

    # Save results to files for review
    with open('matched_files.txt', 'w', encoding='utf-8') as f:
        for match in matches:
            f.write(f"{match['file']}\t{match['slug']}\n")

    with open('unmatched_files.txt', 'w', encoding='utf-8') as f:
        for no_match in no_match_files:
            f.write(f"{no_match['file']}\t{no_match.get('slug', '')}\t{no_match['reason']}\n")

if __name__ == "__main__":
    update_markdown_files('yoast_seo_slugs.csv', 'content')

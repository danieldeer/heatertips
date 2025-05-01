---
author: Daniel Hirsch
category:
  - heater-guides
  - repair
cover:
  alt: diesel heater amps volts multimeter measurement
  image: img/diesel-heater-amps-volts-multimeter-measurement.webp
date: "2023-12-09T15:10:30+00:00"
guid: https://heatertips.com/?p=2277
title: How many Amps does a Diesel Heater use?
url: /how-many-amps-does-a-diesel-heater-use/

---
I did an experiment, measuring the amperage of my diesel heater. This post is about the results.

When you look for diesel heater amperages online, you don’t get any good answers. One website I found said that “diesel heater draws 1 amp per hour”. As an electrical engineer, hearing this hurts my brain. Severely.

That’s as if I say that my car uses 100 horsepower per hour. It’s just a nonsensical use of the unit.

I know the comparison isn’t _exactly_ right, since amps are flow units and hp are power units.

But you get the point.

Let’s have a look at how many amps a diesel heater really uses.

## How many Amps does a Diesel Heater use?

A diesel heater’s amperage profile consists of 3 phases: startup, during heating, and shutoff.

During each phase, diesel heaters do something interesting. Let’s see:

### During Startup

**During startup, a diesel heater draws 8 - 12 Amps.**

The main consumer of the high amperage is the glow plug, which is responsible for initiating the combustion.

The glow plug is essentially an electric resistive heater that draws full amperage until the fuel ignites _and_ the combustion chamber reaches a set operating temperature.

Once the operating temperature is reached, the diesel heater senses that and shuts off the glow plug.

The startup phase, in which the glow plug is turned on, usually takes 3-4 minutes. In very cold conditions it can be up to 5 minutes.

![diesel heater glow plug glowing](/img/diesel-heater-glow-plug-glowing.webp)The glow plug is responsible for the most current draw.

### While Heating

Once the operating temperature is reached, the glow plug turns off and stops drawing electric power.

While heating, 3 other consumers are the main power consumers:

- **Built-in fan:** The built-in fan consumes between 0.25 Amps on the lowest and 2 Amps on the highest fan speed setting.
- **Fuel pump:** The fuel pump also draws a current. But it’s not straightforward to extract a separate amperage for the fuel pump. Likely, it’s around 0.2 Amps on the lowest and around 0.5 Amps on a higher setting.
- **Onboard Electronics:** The built-in electronics, such as the thermostat, draw negligible current. I’d estimate 20mA. Again, this cannot be easily measured.

**While heating, diesel heaters consume anywhere between 0.25 - 2 Amps, depending on the fan and pump settings.**

### When Shutting Off

Here’s where it gets interesting. When shutting a diesel heater off, the amperage goes up again, **rising slowly from 3A to 10A.**

This is counterintuitive because a diesel heater shouldn’t draw electric current during shutoff, should it?

But, as it turns out, **diesel heaters turn on the glow plug when they shut off to vaporize all fuel and grease.**

In that sense, after operation, during the shutoff, diesel heaters self-clean.

Without the glow plug turning on again, the oily grease on the glow plug would harden which causes startup problems the next time you use your diesel heater.

It’s easier to vaporize all grease while it’s still fresh, instead of waiting for the next time you use the heater.

**After the glow plug is done drawing up to 10 Amps to self-clean, the amperage drops to 0 Amps.**

This phase can take anywhere between 1-5 minutes, depending on dirt accumulation and outdoor temperature.

## Useful to Know: Why You Shouldn’t Turn On And Off Your Diesel Heater Often

Because diesel heaters draw a lot of current during startup and shutoff phases, I wonder how much electric energy (in %) is used during these phases.

Let’s assume the following:

- startup phase: 3 minutes at 10 Amps
- heating phase: 8 hours at 0.5 Amps
- shutoff phase: 3 minutes at 10 Amps

I did the calculations and here’s my result:

Based on the provided information, the electric energy used during each phase of the diesel heater's operation is distributed as follows:

- Startup Phase: 10% of the total energy
- Heating Phase: 80% of the total energy
- Shutoff Phase: 10% of the total energy

So, the startup and shutoff phases combined consume 20% of the total electric energy, while the heating phase consumes 80%. ​The combined startup and shutoff phases account for approximately 1.23% of the total operation time.

**Even though the startup and shutoff phase account for only ~1% of the diesel heater operation time, they consume 20% of the electric energy.**

**Turning on and off your diesel heater is a major waste of electric energy. So, carefully evaluate whether it makes more sense to leave the heater running or not in your situation.**

Startup and shutoff phases drain the battery. Minimize them.

## What if You Can’t Supply That Amperage?

If your current power setup can’t supply the necessary amperage for a diesel heater, especially during startup and shutoff phases, you have a few alternatives to consider.

### Option 1: Additional Car Battery

#### Using a Dedicated Car Battery

- **Dedicated Battery**: Consider getting an extra car battery dedicated to the diesel heater. This ensures that your vehicle’s main battery isn’t drained.
- **Parallel Connection**: Connect this additional battery in parallel with your main battery. This arrangement increases the available amperage without changing the voltage.
- **Free Standing**: Alternatively, you could have the extra battery as a standalone system, solely for the heater. This avoids any potential drain on your vehicle’s main battery.

I recommend getting [this **ACDelco truck battery** (click to view it on amazon)](https://www.amazon.com/ACDelco-48AGM-Professional-Automotive-Battery/dp/B008FWCLHU?crid=1DO87AIKO2A1Z&keywords=car%2Bbattery&qid=1702134054&sprefix=car%2Bbatter%2Caps%2C260&sr=8-5&th=1&linkCode=ll1&tag=heatertips-20&linkId=504bc15bb15a86f009e69a8f6fc9d84d&language=en_US&ref_=as_li_ss_tl), because it has a high capacity and thus lasts a longer time without needing to be recharged.

#### Option 2: Diesel Generator

Using a diesel generator to power a diesel heater might seem like a logical step, but it’s not always practical or efficient. Generators are typically designed for higher power outputs and may not be cost-effective or convenient for this purpose. Also, the noise and fuel requirements for a generator could be a downside compared to using a dedicated battery setup.

#### Option 3: Propane Heater as an Alternative

If managing the amperage requirements for a diesel heater is too cumbersome, consider switching to a propane heater.

**Portable propane heaters don’t need any electricity.** They can be a good alternative, especially in situations where electrical power is limited.

However, always compare the efficiency, cost, and practicality of propane heaters in your specific use case before making a decision.

I recommend having a look at this guide: [Diesel vs Propane Heater (5 Differences)](/diesel-vs-propane-heater/)

## Conclusion

In conclusion, while diesel heaters are efficient and effective, their electrical demands during startup and shutoff phases can be a challenge, especially in setups with limited power availability.

Exploring alternatives like an additional car battery, or even switching to a different type of heater, such as a propane heater, can offer practical solutions.

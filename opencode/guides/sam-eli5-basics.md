# SAM — ELI5 Beginner Guide

## What is ServiceNow SAM?

Imagine your company is like a school. The school has:
- Computers in the computer lab
- Tablets in classrooms
- Software programs (like Word, games, learning apps)
- Maintenance contracts for the air conditioning and elevators
- Warranties on all the equipment

**SAM (Service Asset Management)** is like a super-organized notebook that tracks ALL of this. It answers questions like:
- "How many laptops do we have?"
- "Which student has laptop #123?"
- "When does the air conditioner warranty expire?"
- "Are we paying for software nobody uses?"

Without SAM, people use sticky notes, spreadsheets, or memory — and things get lost.

## The Asset Lifecycle (ELI5)

Every asset goes through these stages:

```
Request → Order → Receive → Setup → Give to Someone → Fix when broken → Replace when old → Recycle
```

1. **Request:** Someone says "I need a laptop"
2. **Order:** You buy it from a vendor
3. **Receive:** It arrives, you check it works
4. **Setup:** You install software, put a sticker with a number on it
5. **Give to Someone:** You assign it to an employee
6. **Fix when broken:** It gets repaired
7. **Replace when old:** It's too slow, you get a new one
8. **Recycle:** The old one is wiped and disposed of safely

## Key SAM Words

| Word | What It Means | Real Example |
|------|--------------|--------------|
| Asset | Anything the company owns that's IT-related | A Dell laptop, Microsoft 365 license |
| Asset Tag | A sticker with a unique number | "AST-001234" on the bottom of a laptop |
| Category | What kind of asset it is | Laptop, Monitor, Software, Server |
| Assigned To | Who is using it right now | "Jane Smith" |
| State | Where it is in its life | In Stock, Assigned, In Repair, Retired |
| Contract | Agreement with a company that sells/fixes things | 3-year Dell support contract |
| License | Permission to use software | "100 copies of Microsoft Word" |

## Your First 5 Minutes in SAM

1. **Log in** to ServiceNow
2. **Search** for "Asset" in the navigation
3. **Click** "All" under Asset Management
4. **Look** at the list — do you see any assets?
5. **Click** one to see its details (tag number, who has it, when it was bought)

## Common Questions

**Q: Do I need to buy assets in ServiceNow?**
A: You can create asset records manually, or they can be created automatically when you buy something through the ServiceNow procurement process.

**Q: What happens when someone leaves the company?**
A: Their assets should be returned. SAM helps track this through the offboarding process.

**Q: Can SAM track software too?**
A: Yes! SAM tracks software licenses (how many you have, how many you're using) and installations (which computer has which software).

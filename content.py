"""All website copy lives here. Edit this file, then run `python build.py`."""

SITE = {
    "name": "Atrium Intelligence",
    "url": "https://www.atriumintelligence.net",
    "description": ("Atrium Intelligence brings a small business's sales, marketing, staff and customer "
                    "data into one internal dashboard and one client-facing portal."),
    "email": "atriumintelligence@outlook.com",
    "phone": "860-836-7624",
    "phone_href": "+18608367624",
    "location": "Lebanon, CT 06249",
    "demo_url": "https://smartbrewpitchdemo.streamlit.app/",
}

NAV = [
    {"label": "Services", "href": "index.html#services"},
    {"label": "Live demo", "href": "demo.html"},
    {"label": "About", "href": "index.html#about"},
    {"label": "Contact", "href": "contact.html"},
]

HERO = {
    "title": "All your business data, in one room.",
    "lede": ("Your sales are in the register, your ads are in three apps, your schedule is in a "
             "spreadsheet. We bring it together into one dashboard for your team and a clean portal "
             "for your clients, so you can see what's working and fix what isn't."),
    "primary": {"label": "Explore the live demo", "href": "demo.html"},
    "secondary": {"label": "Talk to us", "href": "contact.html"},
}

# The rooms drawn around the atrium in the hero plan.
PLAN_ROOMS = ["Sales & POS", "Marketing", "Staff & payroll", "Bookkeeping", "Customers", "Reviews"]

PRODUCTS = [
    {
        "name": "Internal dashboard",
        "for": "For you and your managers",
        "summary": ("One place to check the health of the business every morning, with plain-English "
                    "notes on what changed and what to do about it."),
        "areas": [
            ("Operations", "Sales by location and hour, busiest times, staffing gaps, menu or product margins."),
            ("Marketing", "What each channel costs, which customers it brings in, and whether they come back."),
            ("People", "Turnover, tenure, labor cost, and what customers say about service."),
        ],
    },
    {
        "name": "Client portal",
        "for": "For your customers",
        "summary": ("A branded page your business clients can open any time instead of calling or "
                    "emailing you to ask."),
        "areas": [
            ("Orders", "Upcoming deliveries, order history and a simple form to request the next one."),
            ("Invoices", "What's been billed, what's due, and what's been paid."),
            ("Their account", "Who to contact, their ratings, and how on-time you've been for them."),
        ],
    },
]

QUESTIONS = [
    "Which shifts are short-staffed, and by how many people?",
    "Which ads bring in customers who actually come back?",
    "What sells best, and what earns the most per sale?",
    "Why are new hires leaving in their first 90 days?",
    "Which months slow down, and how far?",
    "Which clients have unpaid invoices right now?",
]

SERVICES = [
    {
        "name": "Data cleanup and organization",
        "body": ("We connect the tools you already use, such as your POS, payroll, ad accounts and "
                 "bookkeeping, and turn their exports into one accurate, consistent set of numbers."),
    },
    {
        "name": "Dashboards and reporting",
        "body": ("An internal dashboard for your team and an optional client portal, both built around "
                 "the questions you actually ask, not a generic template."),
    },
    {
        "name": "Forecasting",
        "body": ("Predictive models for demand, staffing and seasonality, so you can schedule, order "
                 "and budget ahead of the slow months and the busy ones."),
    },
]

PROCESS = [
    ("Connect", "We start with a conversation about how your business runs, then link the systems you already use."),
    ("Organize", "We clean and combine the data so every number means the same thing everywhere."),
    ("Build", "We design your dashboards and client portal around your questions, then walk you through them."),
    ("Improve", "We check in regularly and add what you need as the business changes."),
]

ABOUT = {
    "title": "Why “Atrium”",
    "body": [
        ("An atrium is the open room at the center of a building. Light comes in from above, and every "
         "other room opens onto it. That's what we build for your data: one central place where sales, "
         "marketing, staff and customers all come together and are easy to see."),
        ("We're based in Lebanon, Connecticut, and we work with small businesses that have outgrown "
         "spreadsheets but don't need an enterprise software contract."),
    ],
}

DEMO = {
    "title": "Meet Smart Brew",
    "lede": ("Smart Brew Coffee Co. is a made-up coffee shop with three locations. Every number in this "
             "demo is invented, but the dashboards are exactly what we'd build for you."),
    "try": [
        ("Executive Overview", "The cards at the top flag what needs attention, worked out from the data."),
        ("Operations", "Pick Riverside and look at the weekend mornings. The +N marks show how many baristas to add."),
        ("Marketing", "Compare what each channel costs per new customer."),
        ("Smart Brew for Business", "Switch to the client portal and choose a client in “Viewing as.”"),
    ],
    "sleep_note": ("If the demo hasn't been opened in a while, it will show a button to wake it up. "
                   "Click it and the demo will load in about 30 seconds."),
}

CONTACT = {
    "title": "Let's look at your data together",
    "lede": ("Tell us a little about your business and the questions you wish you could answer. "
             "We'll set up a short call and show you what a dashboard could look like for you."),
    "subject": "Dashboard for my business",
}

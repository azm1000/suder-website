# Site-wide content for ssuder.com. Landing-page copy lives in landing_content.py.

FIRM = dict(
    name="Suder, LLC",
    tagline="Counsel for the Built Environment",
    address1="1502 Vine Street, Fourth Floor",
    address2="Cincinnati, Ohio 45202",
    address_note="By appointment only",
    phone="513.694.7500",
    phone_tel="+15136947500",
    email="info@ssuder.com",
    domain="https://www.ssuder.com",
    linkedin="https://www.linkedin.com/in/seansuder/",
    zoneco="https://www.thezoneco.com",
)

# slug -> (nav label, page title)
PRACTICES = [
    ("land-use-zoning", "Land Use & Zoning"),
    ("real-property-litigation", "Real Property Litigation & Appeals"),
    ("real-estate-transactions", "Real Estate Transactions"),
    ("eminent-domain", "Eminent Domain & Takings"),
    ("historic-preservation", "Historic Preservation"),
    ("real-estate-taxation", "Real Estate Taxation"),
    ("local-counsel", "Local Counsel & Co-Counsel"),
]
# short practice-area labels for the CTA slot-machine tagline (settles on FIRM["tagline"])
SPIN_WORDS = [
    "Land Use & Zoning",
    "Eminent Domain",
    "Historic Preservation",
    "Real Estate Taxation",
    "Real Property Litigation",
    "Real Estate Transactions",
    "Local Counsel",
]
# shorter labels for the hero reel, which sets at display size and must not wrap
HERO_SPIN_WORDS = [
    "Zoning",
    "Eminent Domain",
    "Historic Preservation",
    "Real Estate Tax",
    "Litigation",
    "Transactions",
    "Local Counsel",
]
# map landing_content page names -> slug
LANDING_TO_SLUG = {
    "Land Use & Zoning Page": "land-use-zoning",
    "Real Property Litigation & Appeals": "real-property-litigation",
    "Real Estate Transactions": "real-estate-transactions",
    "Eminent Domain & Takings": "eminent-domain",
    "Historic Preservation": "historic-preservation",
    "Real Estate Taxation": "real-estate-taxation",
    "Local Counsel & Co-Counsel Services": "local-counsel",
}
# short blurbs for cards
PRACTICE_BLURBS = {
    "land-use-zoning": "Rezonings, variances, PUDs, appeals, and zoning opinions. At Suder, zoning is not another practice area; it is the practice area.",
    "real-property-litigation": "Trial and appellate counsel in real property disputes, with published decisions in Ohio's courts of appeals.",
    "real-estate-transactions": "Acquisitions, leasing, joint ventures, financings, and condominium structures, handled by former big-firm lawyers.",
    "eminent-domain": "More than 100 property owners represented in appropriation, inverse condemnation, and regulatory takings matters.",
    "historic-preservation": "Certificates of appropriateness, landmark designations, and the fight to keep the buildings worth keeping.",
    "real-estate-taxation": "Valuation challenges before boards of revision and the Board of Tax Appeals, and abatements that make projects pencil.",
    "local-counsel": "Ohio and Northern Kentucky local counsel for national firms, plus Texas and New York transactional counsel.",
}
# hero art per practice: image file (or None for pattern) and a short theme word
PRACTICE_HERO = {
    "land-use-zoning": ("hero-hyde-park.jpg", "Hyde Park Square, Cincinnati: rezoned for a $150M mixed-use project, 2024–2025"),
    "real-property-litigation": ("hero-courthouse.jpg", "Hamilton County Courthouse, home of the First District Court of Appeals"),
    "real-estate-transactions": ("hero-cincinnati-night.jpg", "Downtown Cincinnati, where we closed the Kroger-anchored tower and the Millennium Hotel"),
    "eminent-domain": ("hero-brent-spence.jpg", "The Brent Spence Bridge corridor, Cincinnati"),
    "historic-preservation": ("hero-music-hall.jpg", "Washington Park and Music Hall, Over-the-Rhine, where we saved the 150-year-old bell tower"),
    "real-estate-taxation": ("hero-vine-street.jpg", "Vine Street, Over-the-Rhine, a few blocks from our office"),
    "local-counsel": ("hero-roebling.jpg", "The Roebling Suspension Bridge between Ohio and Kentucky"),
}

# Home hero slideshow: (image, caption)
HOME_SLIDES = [
    ("hero-cincinnati-night.jpg", "Downtown Cincinnati"),
    ("hero-hyde-park.jpg", "Hyde Park Square: rezoned for a $150M mixed-use project"),
    ("hero-music-hall.jpg", "Washington Park, Over-the-Rhine: where we saved the 150-year-old bell tower"),
    ("hero-roebling.jpg", "The Roebling Suspension Bridge: Ohio and Northern Kentucky"),
    ("hero-statehouse.jpg", "The Ohio Statehouse, Columbus"),
    ("hero-toledo.jpg", "Downtown Toledo"),
    ("hero-cleveland.jpg", "Downtown Cleveland"),
    ("hero-city-hall.jpg", "Cincinnati City Hall: where our founder served as Chief Counsel for Land Use and Planning"),
    ("hero-courthouse.jpg", "Hamilton County Courthouse: home of our published appellate wins"),
    ("hero-vine-street.jpg", "Vine Street, Over-the-Rhine: our neighborhood"),
]

# ---------------------------------------------------------------- results
# Only verified matters. Each: slug, title, meta (place/year), summary, practices (slugs), featured
RESULTS = [
    dict(slug="hyde-park-square", img="r-hyde-park.jpg", title="Hyde Park Square rezoning", meta="Cincinnati · 2024–2025",
         kicker="Infill development",
         summary="Lead counsel for the successful effort to rezone a portion of Hyde Park Square for a $150,000,000 mixed-use development with apartments, a boutique hotel, and underground parking. A high-profile, contested neighborhood approval.",
         practices=["land-use-zoning"], featured=True),
    dict(slug="washington-park-bell-tower", img="r-bell-tower.jpg", title="Saving the Washington Park bell tower", meta="Over-the-Rhine · 2022–2023",
         kicker="Historic preservation",
         summary="Lead counsel for the successful effort to save the 150-year-old church bell tower on Washington Park, including multiple emergency court orders, personally argued and won by J.P. Burleigh, that halted demolition in the Over-the-Rhine Historic District.",
         practices=["historic-preservation", "real-property-litigation"], featured=True),
    dict(slug="crosley-building", img="r-crosley.jpg", title="Crosley Building adaptive reuse", meta="Camp Washington · 2020–2021",
         kicker="Historic adaptive reuse",
         summary="Lead land use counsel for the $50 million conversion of the former Crosley Radio Corp. headquarters into 175 to 250 apartments, with a focus on providing units to artists.",
         practices=["land-use-zoning", "historic-preservation"], featured=True),
    dict(slug="south-lebanon-multifamily", title="Trail-oriented multifamily", meta="South Lebanon, Ohio · 2020",
         kicker="Rezoning",
         summary="Lead land use counsel on the rezoning that permitted 416 apartments across eight buildings on the Little Miami River Trail. Now under construction.",
         practices=["land-use-zoning"]),
    dict(slug="st-vincent-de-paul", title="St. Vincent de Paul outreach center", meta="West End · 2018",
         kicker="Rezoning",
         summary="Lead land use counsel on the rezoning for a new 36,000-square-foot facility for the Society of St. Vincent de Paul Cincinnati, including an expanded food pantry, charitable pharmacy, homelessness-prevention services, chapel, health clinic, and call center.",
         practices=["land-use-zoning"]),
    dict(slug="pendleton-senior-housing", img="r-pendleton.jpg", title="Affordable senior housing in the historic urban core", meta="Pendleton, Cincinnati · 2026",
         kicker="Entitlements",
         summary="Suder helped secure a key approval for an affordable senior housing project in one of Cincinnati's historic neighborhoods after the design was reworked to respect its context. Proof that the firm gets projects built in historic districts, not just blocked.",
         practices=["land-use-zoning", "historic-preservation"]),
    dict(slug="miller-v-cincinnati", img="r-city-hall.jpg", title="Taxpayer standing: Cincinnati ex rel. Miller v. Cincinnati", meta="2024-Ohio-4805 (1st Dist.)",
         kicker="Published opinion",
         summary="Representing the affordable housing developer, Over-the-Rhine Community Housing, Suder defeated a taxpayer suit attacking the City ordinance that approved the project. The First District vacated the judgment and ordered the case dismissed for lack of standing.",
         practices=["real-property-litigation"], featured=True),
    dict(slug="cook-v-lockland", img="r-courthouse.jpg", title="Nonconforming uses: Cook v. Lockland", meta="2024-Ohio-9 (1st Dist.)",
         kicker="Published opinion",
         summary="Representing a property owner against the Village of Lockland, Suder won a reversal holding that the village, not the owner, bears the burden of proving a nonconforming use was abandoned before it can strip the owner's vested right to continue it.",
         practices=["real-property-litigation", "eminent-domain"]),
    dict(slug="mt-lookout", img="r-courthouse-2.jpg", title="Use variances: Mt. Lookout Community Council v. Cincinnati", meta="2023-Ohio-1729 (1st Dist.)",
         kicker="Published opinion",
         summary="Representing the neighborhood community council, Suder won a reversal vacating a use variance that would have allowed the demolition of four buildings in Mt. Lookout. The court held that demolition is not a land use that can be permitted through a use variance.",
         practices=["real-property-litigation", "historic-preservation"]),
    dict(slug="kroger-tower", img="r-downtown.jpg", title="Grocery-anchored downtown tower", meta="Downtown Cincinnati · 2018",
         kicker="Sale-leaseback financing",
         summary="Lead transactional counsel on the sale-leaseback financing for a new 18-story downtown apartment tower anchored by a new multi-level Kroger store.",
         practices=["real-estate-transactions"], featured=True),
    dict(slug="millennium-hotel", img="r-millennium.jpg", title="Convention hotel acquisition", meta="Downtown Cincinnati · 2020",
         kicker="Acquisition",
         summary="Lead transactional counsel on the acquisition of the 32-story Millennium Hotel across from the Duke Energy Convention Center.",
         practices=["real-estate-transactions"]),
    dict(slug="assisted-living-portfolio", img="r-roebling.jpg", title="$100 million assisted living portfolio", meta="Ohio, Kentucky, and Indiana · 2020",
         kicker="Sale-leaseback financing",
         summary="Lead real estate counsel on the sale-leaseback financing of a $100,000,000 assisted living portfolio spanning three states.",
         practices=["real-estate-transactions", "local-counsel"]),
    dict(slug="orthodontics-leases", title="Retail leasing program for a growing orthodontics group", meta="Greater Cincinnati and Northern Kentucky · 2019",
         kicker="Retail leasing",
         summary="Lead leasing counsel for locations in several of the region's top retail centers, including Kenwood Towne Centre.",
         practices=["real-estate-transactions"]),
    dict(slug="playhouse-square-tower", img="r-playhouse.jpg", title="Playhouse Square residential tower", meta="Downtown Cleveland · opened 2020",
         kicker="Public financing",
         summary="Counsel on matters related to a portion of the public financing for a new 34-story apartment tower on Cleveland's historic Playhouse Square.",
         practices=["real-estate-transactions", "local-counsel"]),
    dict(slug="w-austin", img="r-w-austin.jpg", title="W Austin Hotel & Residences condominium", meta="Austin, Texas",
         kicker="Condominium structuring",
         summary="Josh Bernstein prepared the condominium documents for the W Austin Hotel & Residences, the mixed-use tower combining a hotel, private residences, and commercial space, using the condominium regime to allocate ownership, control, and cost among very different uses in one building.",
         practices=["real-estate-transactions"], featured=True),
    dict(slug="the-grove", img="r-austin.jpg", title="The Grove: 75 acres of state land into a walkable mixed-use community", meta="Austin, Texas",
         kicker="Land acquisition and development",
         summary="Josh Bernstein represented the private equity-backed developer in acquiring 75 acres of state-owned land in central Austin through a public bid process, including leaseback agreements with multiple state agencies, public procurement requirements, and affordable housing commitments, followed by the ongoing development, leasing, and parcel sales for the community.",
         practices=["real-estate-transactions"]),
    dict(slug="barton-creek-mueller", img="r-mueller.jpg", title="Austin's marquee master-planned communities", meta="Barton Creek and Mueller · Austin, Texas",
         kicker="Master-planned communities",
         summary="Josh Bernstein was heavily involved in the development, condominium, and covenant work for several of the projects that shaped Austin's growth, including Barton Creek and the Mueller redevelopment.",
         practices=["real-estate-transactions"]),
    dict(slug="age-restricted-condominium", title="Age-restricted communities structured as condominiums", meta="Texas",
         kicker="Condominium as land-planning tool",
         summary="For a master-planned community developer, Josh Bernstein built a condominium structure for subdividing all of the land in multiple 55+ communities, unlocking significantly more density than a traditional platted subdivision would allow, and handled sales of improved and unimproved parcels to sub-developers, homebuilders, and individuals.",
         practices=["real-estate-transactions"]),
    dict(slug="timeshare-conversion", title="First-of-its-kind timeshare conversion", meta="National hospitality company",
         kicker="Acquisition and entitlements",
         summary="Josh Bernstein represented a national hospitality company in acquiring a Class A apartment building and converting it to timeshare use, securing a first-of-its-kind approval from local authorities, then structuring multiple condominium regimes to support a multi-club timeshare program and state timeshare registrations.",
         practices=["real-estate-transactions"]),
    dict(slug="homebuilder-land-program", title="Land acquisition program for a publicly traded homebuilder", meta="Texas",
         kicker="Land acquisition",
         summary="Josh Bernstein advised a public homebuilder on the simultaneous acquisition of dozens of unimproved parcels, negotiating entitlement and development agreements and utility and shared-facility agreements with sellers and neighbors, with a tracking system built to keep the volume on schedule.",
         practices=["real-estate-transactions"]),
    dict(slug="san-diego-joint-venture", title="Joint venture for a major commercial and mixed-use project", meta="San Diego, California",
         kicker="Joint venture",
         summary="Josh Bernstein represented an institutional developer in structuring and negotiating the joint venture for a large commercial and mixed-use development in San Diego.",
         practices=["real-estate-transactions", "local-counsel"]),
    dict(slug="lender-representation", title="Commercial lender representation, including a distressed Houston project", meta="Nationwide",
         kicker="Lending and workouts",
         summary="Josh Bernstein has represented a commercial real estate lender across multiple loans nationwide, including a Houston development where the borrower's deal collapsed and the lender foreclosed and resold the asset.",
         practices=["real-estate-transactions", "local-counsel"]),
]

OPINIONS = [
    ("Taxpayer standing", "Cincinnati ex rel. Miller v. Cincinnati", "2024-Ohio-4805 (1st Dist.)",
     "https://www.supremecourt.ohio.gov/rod/docs/pdf/1/2024/2024-Ohio-4805.pdf", "miller-v-cincinnati"),
    ("Nonconforming uses; abandonment of property rights", "Cook v. Lockland", "2024-Ohio-9 (1st Dist.)",
     "https://www.supremecourt.ohio.gov/rod/docs/pdf/1/2024/2024-Ohio-9.pdf", "cook-v-lockland"),
    ("Use variances", "Mt. Lookout Cmty. Council v. Cincinnati", "2023-Ohio-1729 (1st Dist.)",
     "https://www.supremecourt.ohio.gov/rod/docs/pdf/1/2023/2023-Ohio-1729.pdf", "mt-lookout"),
    ("Writ of mandamus", "State ex rel. 506 Phelps Holdings, LLC v. Cincinnati Union Bethel", "2013-Ohio-388 (1st Dist.)",
     "https://www.supremecourt.ohio.gov/rod/docs/pdf/1/2013/2013-Ohio-388.pdf", None),
    ("Spot zoning; legislative variances", "State ex rel. Phillips Supply Co. v. Cincinnati", "2012-Ohio-6096 (1st Dist.)",
     "https://www.supremecourt.ohio.gov/rod/docs/pdf/1/2012/2012-Ohio-6096.pdf", None),
    ("Summary judgment in foreclosure", "HillStreet Fund III, L.P. v. Bloom", "2010-Ohio-2267 (2d Dist.)",
     "https://www.supremecourt.ohio.gov/rod/docs/pdf/2/2010/2010-Ohio-2267.pdf", None),
]

JURISDICTIONS = """Anderson Township|Boone County, KY|Butler County|City of Akron|City of Beavercreek|City of Bellevue, KY|City of Blue Ash|City of Canal Winchester|City of Centerville|City of Cincinnati|City of Cleveland Heights|City of Columbus|City of Fairborn|City of Fairfield|City of Florence, KY|City of Forest Park|City of Franklin|City of Ft. Wright, KY|City of Hamilton|Henry County|City of Kettering|City of Lebanon|City of Loveland|City of Madeira|City of Mason|City of McComb|City of Milford|City of Monroe|City of Montgomery|City of Norwood|City of Oxford|City of Piqua|City of Springboro|City of Springdale|City of Toledo|City of The Village of Indian Hill|City of Union, KY|City of Vandalia|City of West Chester|City of Westlake|City of Wyoming|Clermont County|Colerain Township|Deerfield Township|Fairfield Township|Goshen Township|Green Township|Hamilton County|Harrison Township|Kenton County, KY|Liberty Township|Miami Township|Pierce Township|Sycamore Township|Symmes Township|Village of Addyston|Village of Evendale|Village of Gates Mills|Village of Kirtland Hills|Village of Lockland|Village of South Lebanon|Village of Woodlawn|Warren County|Washington Township|West Chester Township""".split("|")

AWARDS = [
    # url="" renders the badge as plain artwork; set one and it becomes a link to the listing
    dict(img="badge-best-lawyers-loty-2026.png", alt="Best Lawyers Lawyer of the Year 2026, Sean S. Suder, Land Use and Zoning Law, Cincinnati",
         title="Lawyer of the Year 2026", sub="Best Lawyers · Land Use and Zoning Law · Cincinnati", url=""),
    dict(img="badge-chambers-2026.png", alt="Chambers USA Top Ranked 2026, Sean Suder",
         title="Chambers USA, Band 1", sub="Ohio Real Estate: Zoning/Land Use, every year since 2019", url=""),
    dict(img="badge-best-law-firms-2026.png", alt="Best Law Firms 2026, ranked by Best Lawyers",
         title="Best Law Firms 2026", sub="Ranked by Best Lawyers · United States", url=""),
    dict(img=None, alt="", title="Chambers Spotlight Firm", sub="Cincinnati Real Estate · 2025 and 2026", url=""),
]

CREDENTIALS = [
    ("60+", "jurisdictions across Ohio and Northern Kentucky where we have handled zoning matters"),
    ("Band 1", "Chambers USA ranking for Sean Suder in Ohio Real Estate: Zoning/Land Use, every year since 2019"),
    ("100+", "property owners represented in eminent domain and takings matters"),
    ("5", "states of licensure: Ohio, Kentucky, Texas, New York, and Washington, D.C."),
]

TEAM = [
    dict(slug="sean-suder", first="Sean", name="Sean S. Suder", suffix="Esq., LEED AP", role="Managing Member / Founder",
         email="sean@ssuder.com", phones="513.694.7501 (d) · 513.235.3470 (c)", img="sean",
         intro="Sean has devoted his entire adult life to working in service to those who make, work with, manage, and contribute to the built environment.",
         bio=[
             "Sean earned an urban planning degree from architecture school, worked in city planning and construction management before law school, practiced in a large commercial real estate and land use practice after law school, served nearly four years as a large city government's chief land use attorney, became a partner in top commercial real estate and land use practices in mid-size and large law firms, and has founded and led zoning consulting firms with a national reach.",
             "All of this led him to form a first-in-class boutique commercial real estate and land use law firm reflective of his passion for being Counsel for the Built Environment.",
         ],
         sections=[
             ("Experience", [
                 "City of Cincinnati Chief Counsel for Land Use and Planning (2010–2014): counsel to the City Planning Commission, Zoning Board of Appeals, Historic Conservation Board, Board of Building Appeals, and Board of Housing Appeals; lead counsel for the City's land development code and its award-winning historic preservation ordinance; lead trial counsel on land use and zoning matters",
                 "Partner, Calfee, Halter & Griswold LLP (2016–2020) and Graydon Head & Ritchey LLP, now Bricker Graydon (2014–2016); attorney, Keating Muething & Klekamp PLL (2004–2010)",
                 "Founder and CEO, ZoneCo (2020–present), a national zoning consulting firm; dozens of zoning code rewrites, including Palm Beach, Florida; Southold, New York; Hilton Head Island, South Carolina; and Rockville, Maryland",
                 "Construction management in the Washington, D.C. area before law school",
             ]),
             ("Knowledge", [
                 "Adjunct Professor of Land Use and Development Law, University of Cincinnati College of Law",
                 "Frequent speaker on land use and zoning at national, regional, and local conferences",
                 "Creator and host of Zonecasts; member, APA Law & Planning Digest Advisory Board",
             ]),
             ("Education", [
                 "J.D., University of Virginia School of Law (2004)",
                 "Bachelor of Urban and Environmental Planning, University of Virginia School of Architecture (2000), with honors",
                 "Founder, University of Virginia Collegiate Mock Trial program; UVA Honor Committee; Raven Society",
             ]),
             ("Credentials", [
                 "Licensed attorney: Ohio, Kentucky, Washington, D.C.",
                 "Licensed title agent, Ohio; LEED AP",
                 "Admitted, U.S. District Court for the Southern District of Ohio",
             ]),
             ("Peer reviewed", [
                 "Best Lawyers \"Lawyer of the Year\" 2026, Land Use and Zoning Law, Cincinnati; The Best Lawyers in America, Real Estate Law and Land Use and Zoning Law (2019–2026)",
                 "\"Leading Lawyer,\" Chambers USA, Band 1 in Ohio Real Estate: Zoning/Land Use (every year since 2019)",
                 "Ohio Super Lawyers and Ohio Rising Stars (2007, 2009, 2016–2018)",
             ]),
         ]),
    dict(slug="jp-burleigh", first="J.P.", name="J.P. Burleigh", suffix="Esq.", role="Member",
         email="jp@ssuder.com", phones="513.694.7502 (d) · 513.404.5776 (c)", img="jp",
         intro="J.P.'s legal practice is devoted exclusively to real property: land and the things built on it.",
         bio=[
             "J.P.'s fascination with property began in an unlikely place. An avid fisherman, he brings a rod with him almost anywhere he goes. While living (and fishing) in Scotland for a semester during college, he was surprised to learn that land and water rights are treated very differently there than in the United States. Everyone in Scotland enjoys a \"right to roam\" across the countryside, even through private land, but all rivers and streams are privately owned, so fishing licenses are bought from individual landowners rather than from the state. The experience opened his eyes to how property law shapes the ways we all use, enjoy, and interact with the world around us.",
             "J.P. guides clients through residential and commercial real estate transactions, including contract negotiation, due diligence, and closing, and often negotiates commercial leases of office and retail space. For clients looking to develop property, he has a keen understanding of the processes to obtain land use and zoning approvals, and he especially enjoys advocating before administrative boards.",
             "He also prides himself on helping clients resolve real property disputes efficiently, whether a deal gone bad, an unfavorable zoning decision, or a disagreement with a neighbor, using mediation and informal negotiation where possible. When negotiation is not an option, he thrives on vindicating his clients' interests in court, including personally arguing for and obtaining multiple emergency court orders to prevent the demolition of a historic church bell tower in Cincinnati's Over-the-Rhine Historic District.",
         ],
         sections=[
             ("Experience", [
                 "Consults with and serves as legal counsel to ZoneCo LLC on rewriting land use and zoning regulations for local governments around the country",
                 "Village of Mariemont, Ohio Planning Commissioner",
                 "Hamilton County Court of Common Pleas (intern, 2019); U.S. District Court for the Southern District of Ohio (intern, 2020)",
             ]),
             ("Knowledge", [
                 "Former contributor and editor, University of Cincinnati Law Review Blog, frequently writing on land use issues (2019–2021)",
                 "Winner of the John R. Sayler Prize in Evidence (2019)",
             ]),
             ("Education", [
                 "J.D., University of Cincinnati College of Law, cum laude",
                 "B.A., Political Science, Furman University, magna cum laude",
             ]),
             ("Credentials", [
                 "Licensed attorney: Ohio",
                 "Admitted, U.S. District Court for the Southern District of Ohio",
                 "Admitted pro hac vice in courts in Kentucky and West Virginia",
             ]),
         ]),
    dict(slug="teresa-bamberger", first="Teresa", name="Teresa Bamberger", suffix="Esq., AICP", role="Of Counsel",
         email="teresa@ssuder.com", phones="513.694.7500 (o) · 513.587.9242 (c)", img="teresa",
         intro="Teresa's path to land use law began in architecture school, where she developed a passion for community planning and urban design.",
         bio=[
             "Early in her career Teresa was an urban planner, designing large multi-use projects, community plans, and architectural guidelines. She then served as Town Planner for a small, rapidly growing community, where she engaged the community in completely rewriting the Town's Comprehensive Plan and Zoning Code. Later, as a planner and civil engineering project manager, she designed and managed large site development projects from inception through construction.",
             "Her interest in the laws that shape and regulate community development led her to law school. As an attorney, Teresa's background in the nuts and bolts of site development, permitting, community engagement, and site design enables her to find creative, efficient, and sometimes surprising solutions to complex land use disputes.",
             "Teresa is committed to obtaining the best outcome for her clients through negotiation or mediation when possible, and she will zealously advocate for her client if a dispute must go to trial.",
         ],
         sections=[
             ("Experience", [
                 "Land use, zoning, and real estate attorney with extensive experience in eminent domain (2011–present)",
                 "Planning and civil engineering project manager, responsible for initial design through construction of large site development projects (1996–2001)",
                 "Urban design and community planner on award-winning projects at a national architecture and engineering firm (1987–1991)",
             ]),
             ("Knowledge", [
                 "Successfully represented over 100 clients in eminent domain and takings matters",
                 "Represented numerous clients in land use litigation, permitting, easements, variances, public hearings, and community engagement",
                 "As chairperson of a county Environmental Affairs Board, contributed to drafting a Maryland county's first forest conservation ordinance; committee member for stormwater best-management practices in the State of Maryland",
             ]),
             ("Education", [
                 "J.D., University of Cincinnati College of Law, cum laude",
                 "B.Arch., University of Detroit, cum laude",
             ]),
             ("Credentials", [
                 "Licensed attorney: Ohio",
                 "AICP, American Institute of Certified Planners",
                 "Admitted, U.S. District Courts for the Southern and Northern Districts of Ohio",
             ]),
         ]),
    dict(slug="josh-bernstein", first="Josh", name="Josh Bernstein", suffix="Esq.", role="Of Counsel",
         email="josh@ssuder.com", phones="513.694.7500 (o) · 512.921.3269 (c)", img="josh",
         intro="Josh is a Cincinnati native and real estate and corporate attorney who spent more than two decades in Austin, Texas, advising developers, investors, and operators through the deals that shaped it.",
         bio=[
             "Josh began his career as a mergers and acquisitions and securities associate at an elite New York firm before returning to Austin, where he attended law school at the University of Texas, joining Armbrust & Brown, Austin's go-to firm for land use and development work. There he worked on formative projects that helped define the city's transformation into a thriving metropolis and gained a deep understanding of \"dirt\" real estate law: all of the pieces and moving parts that go into taking a project from raw land to a finished, financed, and occupied development.",
             "As he moved into partnership roles at Greenberg Traurig and Norton Rose Fulbright, Josh broadened his practice to development-driven transactions and real estate finance and private equity: acquisitions, dispositions, and leasing; joint ventures, debt and equity financing, and fund formation; across every asset class, from single-family and multifamily to industrial, office, retail, and hotel, with particular depth in senior housing. He is a recognized authority on structuring complex condominiums for the financing and sale of commercial, residential, and mixed-use projects, including the W Austin Hotel & Residences and Austin's marquee master-planned communities.",
             "Josh now lives in downtown Cincinnati, a short walk from the firm's offices on Vine Street, bringing his boomtown experience home. He is an urbanist who believes deeply in the power of human connection through the kind of chance encounters that can only happen in walkable, dense environments, and he takes pride in helping his clients serve as placemakers for those spaces. Outside the office, Josh is an instrument-rated private pilot and a lifelong aviation enthusiast, with a passion for modern architecture and design. He is the father of two daughters, Noa and Ada.",
         ],
         sections=[
             ("Experience", [
                 "Of Counsel, Hajjar Peters (2020–2025); Partner, Norton Rose Fulbright, Austin and New York (2017–2020); Partner, Greenberg Traurig, Austin (2014–2017); Associate to Partner, Armbrust & Brown, Austin (2004–2014); Associate, Skadden, Arps, Slate, Meagher & Flom, New York (2002–2004)",
                 "Numerous condominium and master-planned community projects; joint ventures, portfolio acquisitions, and complex real estate financings; public and private company M&A",
             ]),
             ("Education", [
                 "J.D., University of Texas School of Law (2002)",
                 "B.A., Spanish, The Ohio State University (1998), magna cum laude, with honors",
             ]),
             ("Credentials", [
                 "Licensed attorney: Texas (2005), New York (2002); Ohio application in progress",
                 "Active member, CREDA Cincinnati (Commercial Real Estate Development Association)",
                 "Fluent in Spanish",
             ]),
         ]),
    dict(slug="todd-kinskey", first="Todd", name="Todd Kinskey", suffix="FAICP", role="City Planner (non-attorney)",
         email="tkinskey@thezoneco.com", phones="513.497.0500 (d)", img="todd",
         intro="Todd brings more than three decades of local government planning, zoning, subdivision, housing policy, and project management experience to the firm's clients.",
         bio=[
             "Todd Kinskey, FAICP, is the immediate past Director of the Department of Planning, Neighborhoods & Development for the City of Dayton, Ohio, and the former Hamilton County, Ohio Director of Planning + Development. He has led numerous code update and rewrite projects for complex and diverse built environments during his 30-plus years in public service.",
             "He is a committed, caring, and thoughtful city planner whose work has been recognized by the American Planning Association through his induction into the College of Fellows of the AICP (FAICP) in 2020. Todd has served as APA Ohio President, on the City of Cincinnati Board of Zoning Appeals, and as an Adjunct Professor of City Planning at the University of Cincinnati College of Design, Art, Architecture, and Planning (DAAP), among many other roles.",
         ],
         sections=[
             ("Experience", [
                 "Director, Department of Planning, Neighborhoods & Development, City of Dayton (2018–2024)",
                 "Director of Planning + Development, Hamilton County, Ohio",
                 "Zoning code rewrites for Hamilton County and the Villages of Greenhills, Fairfax, Elmwood Place, North Bend, and Crosby Township; comprehensive plans for Dayton, Hamilton County, Fairfax, Greenhills, and Trenton",
                 "Senior City Planner and Project Manager, ZoneCo",
             ]),
             ("Leadership", [
                 "APA Ohio Chapter President (2015–2016), Vice President, Secretary, and Legislative Chair",
                 "City of Cincinnati Zoning Board of Appeals (2008–2011); Plan Cincinnati Steering Committee; Brent Spence Bridge Design Committee",
                 "ULI Cincinnati Advisory Board (2019–2024); Montgomery County Land Bank Board of Directors (2018–2024)",
             ]),
             ("Education", [
                 "Bachelor of Urban Planning, cum laude, with a Certificate in Historic Preservation, University of Cincinnati College of Design, Art, Architecture, and Planning (DAAP)",
             ]),
             ("Credentials", [
                 "American Institute of Certified Planners (AICP) since 1997; AICP College of Fellows (FAICP), Class of 2020",
             ]),
         ]),
]

# Old Squarespace URLs -> new pages
REDIRECTS = [
    ("/suder", "/team/sean-suder"),
    ("/jpb", "/team/jp-burleigh"),
    ("/tb-1", "/team/teresa-bamberger"),
    ("/tb-1-1", "/team/josh-bernstein"),
    ("/professionals", "/team"),
    ("/publishedopinions", "/opinions"),
    ("/new-dropdown", "/opinions"),
    ("/experience", "/results"),
    ("/jurisdictions", "/jurisdictions"),
    ("/zoning-letters-opinions", "/zoning-letters"),
    ("/land", "/practice/real-estate-transactions"),
    ("/retailleasing", "/practice/real-estate-transactions"),
    ("/officeleasing", "/practice/real-estate-transactions"),
    ("/industrialleasing", "/practice/real-estate-transactions"),
    ("/careers", "/careers"),
    ("/termsofuse", "/terms"),
    ("/cart", "/"),
]

# Photo credits (Wikimedia Commons). Filled by build; (file name, title on Commons, author, license, license url)
PHOTO_CREDITS = [('hero-hyde-park.jpg', 'The Kilgour Fountain at Hyde Park Square', 'EEJCC', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:The_Kilgour_Fountain_at_Hyde_Park_Square.jpg'), ('r-hyde-park.jpg', 'Hyde Park Square views', 'EEJCC', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Hyde_Park_Square_views.jpg'), ('hero-courthouse.jpg', 'Hamilton County Courthouse, Cincinnati, OH', 'Warren LeMay', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Hamilton_County_Courthouse,_Cincinnati,_OH.jpg'), ('r-courthouse.jpg', 'Hamilton County Courthouse, Cincinnati, OH (46629997544)', 'Warren LeMay', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Hamilton_County_Courthouse,_Cincinnati,_OH_(46629997544).jpg'), ('hero-cincinnati-night.jpg', 'Downtown Cincinnati skyline at night', 'EEJCC', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Downtown_Cincinnati_skyline_at_night.jpg'), ('hero-brent-spence.jpg', 'Brent Spence Bridge 2025h', 'Antony-22', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Brent_Spence_Bridge_2025h.jpg'), ('r-brent-spence.jpg', 'Brent Spence Bridge 2025f', 'Antony-22', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Brent_Spence_Bridge_2025f.jpg'), ('hero-music-hall.jpg', 'Cincinnati Music Hall', 'Fred Haaser', 'CC BY 3.0', 'https://creativecommons.org/licenses/by/3.0', 'https://commons.wikimedia.org/wiki/File:Cincinnati_Music_Hall_(42707046).jpeg'), ('r-bell-tower.jpg', 'Washington Park and Cincinnati Music Hall', 'David Brossard', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://commons.wikimedia.org/wiki/File:Washington_Park_and_Cincinnati_Music_Hall_(11782887063).jpg'), ('hero-vine-street.jpg', 'Vine Street, Over-the-Rhine, Cincinnati, OH', 'Warren LeMay', 'CC0', 'http://creativecommons.org/publicdomain/zero/1.0/deed.en', 'https://commons.wikimedia.org/wiki/File:Vine_Street,_Over-the-Rhine,_Cincinnati,_OH_(33711708098).jpg'), ('hero-roebling.jpg', 'John A. Roebling Suspension Bridge', 'redlegsfan21', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://commons.wikimedia.org/wiki/File:John_A._Roebling_Suspension_Bridge_(16165298856).jpg'), ('r-roebling.jpg', 'Cincinnati Skyline from Roebling Bridge, Covington, KY', 'w_lemay', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://commons.wikimedia.org/wiki/File:Cincinnati_Skyline_from_Roebling_Bridge,_Covington,_KY.jpg'), ('r-crosley.jpg', 'Crosley Building 2', 'Hhelvey', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Crosley_Building_2.jpg'), ('r-city-hall.jpg', 'Cincinnati City Hall, Cincinnati, OH', 'w_lemay', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://commons.wikimedia.org/wiki/File:Cincinnati_City_Hall,_Cincinnati,_OH.jpg'), ('r-playhouse.jpg', 'Cleveland Playhouse Square', 'Erik Drost', 'CC BY 2.0', 'https://creativecommons.org/licenses/by/2.0', 'https://commons.wikimedia.org/wiki/File:Cleveland_Playhouse_Square_(13917562719).jpg'), ('r-w-austin.jpg', 'W Hotel Austin, June 2010', 'LoneStarMike', 'CC BY-SA 3.0', 'https://creativecommons.org/licenses/by-sa/3.0', 'https://commons.wikimedia.org/wiki/File:WHotelAustin-Jun2010.JPG'), ('r-austin.jpg', 'Downtown Austin Skyline - Lady Bird Lake', 'ajay_suresh', 'CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0', 'https://commons.wikimedia.org/wiki/File:Downtown_Austin_Skyline_-_Lady_Bird_Lake_(54987239041).jpg'), ('r-millennium.jpg', 'Millennium Hotel Cincinnati Exterior', 'millenniumcincinnati', 'CC BY 2.0', 'https://creativecommons.org/licenses/by/2.0', 'https://commons.wikimedia.org/wiki/File:Millennium_Hotel_Cincinnati_Exterior.jpg'), ('r-mueller.jpg', 'Mueller lake park and hangar 2014', 'Larry D. Moore', 'CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0', 'https://commons.wikimedia.org/wiki/File:Mueller_lake_park_and_hangar_2014.jpg')]

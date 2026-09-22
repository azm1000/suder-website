from site_content import JURISDICTIONS

# One source of truth for the jurisdiction count: the list itself. Every "N
# jurisdictions" claim on the site reads it, so the number can never drift from
# what /jurisdictions/ actually shows.
NJ = len(JURISDICTIONS)

# Content for the seven Suder, LLC practice-area landing pages.
# Each page: image_desc, image_text, licensed, heading, subheading, button,
# description, bullets (list), results (list of (title, text)).

LICENSED = ("Licensed in Ohio, Kentucky, Texas, New York, and Washington, D.C., with "
            "co-counsel relationships nationwide")

FLAG = "[FOR SEAN TO CONFIRM/PROVIDE] "
JFLAG = "[FOR JOSH TO PROVIDE] "

PAGES = [
    # ------------------------------------------------------------------ 1
    dict(
        name="Land Use & Zoning Page",
        image_desc=(
            "Real project photo preferred: Hyde Park Square in Cincinnati (the block "
            "Suder rezoned in 2024-2025 for a $150M mixed-use project), shot at street "
            "level or from above so the neighborhood context reads. Second choice: a "
            "Cincinnati City Hall council chamber or Planning Commission hearing room "
            "with the dais in view (Suder appears before these boards constantly). Stock "
            "fallback: a zoning map or site plan spread on a table with a downtown "
            "skyline in the background. Avoid generic gavels and handshakes."
        ),
        image_text="Counsel for the Built Environment",
        heading="Ohio's Land Use & Zoning Counsel",
        subheading=(
            "Getting a project approved takes more than knowing the code; it takes "
            "knowing how the staff, the boards, and the neighbors actually work. "
            "Suder's lawyers have sat on every side of that table, from city hall to the "
            "hearing room, and we use that experience to move your project from concept "
            "to approval."
        ),
        button="Start Your Project",
        description=(
            "At Suder, zoning and land use law is not just another practice area; it is "
            "the practice area. Our founder, Sean Suder, served nearly four years as the "
            "City of Cincinnati's Chief Counsel for Land Use and Planning, was lead "
            "counsel for the City's land development code, and now rewrites zoning codes "
            "for cities across the country through his consulting firm, ZoneCo. That "
            f"inside knowledge, applied in {NJ} jurisdictions across Ohio and "
            "Northern Kentucky, is why Chambers USA has ranked Sean in Band 1 for Ohio "
            "Real Estate: Zoning/Land Use every year since 2019."
        ),
        bullets=[
            "Rezonings and planned unit developments (PUDs)",
            "Variances, special exceptions, and conditional use approvals",
            "Zoning opinions and verification letters for lenders and closings (Ohio, Kentucky, and D.C.)",
            "Administrative appeals of zoning and planning decisions",
            "Zoning code drafting, interpretation, and expert witness services",
            "Public records requests and entitlement due diligence for acquisitions",
        ],
        results=[
            ("Hyde Park Square rezoning (Cincinnati, 2024-2025)",
             "Lead counsel for the successful rezoning of a portion of Hyde Park Square for a "
             "$150,000,000 mixed-use development with apartments, a boutique hotel, and "
             "underground parking. A high-profile, contested neighborhood approval."),
            ("Trail-oriented multifamily (South Lebanon, Ohio, 2020)",
             "Lead land use counsel on the rezoning that permitted 416 apartments in eight "
             "buildings on the Little Miami River Trail. Now under construction; good "
             "before-and-after photo opportunity."),
            ("Crosley Building adaptive reuse (Camp Washington, 2020-2021)",
             "Lead land use counsel for the $50 million conversion of the former Crosley "
             "Radio Corp. headquarters into 175-250 apartments with units set aside for artists."),
            ("St. Vincent de Paul outreach center (West End, 2018)",
             "Lead land use counsel on the rezoning for a new 36,000-square-foot facility "
             "with an expanded food pantry, charitable pharmacy, health clinic, and "
             "homelessness-prevention services."),
            ("Affordable senior housing approval (Pendleton, September 2026)",
             "Suder (Sean Suder and J.P. Burleigh) helped secure a key approval for an "
             "affordable senior housing project in Cincinnati's historic urban core after "
             "the design was reworked to fit the neighborhood (covered by the Cincinnati "
             "Business Courier)."),
        ],
    ),
    # ------------------------------------------------------------------ 2
    dict(
        name="Real Property Litigation & Appeals",
        image_desc=(
            "Real location preferred: the Hamilton County Courthouse in downtown "
            "Cincinnati (home of the Common Pleas court and the Ohio First District Court "
            "of Appeals, where most of Suder's published decisions were won), exterior "
            "columns or the main entrance. Stock fallback: an appellate courtroom or "
            "bound Ohio appellate reports on a shelf. No gavel-and-scales cliches."
        ),
        image_text="Counsel for the property owner",
        heading="Real Property Trial & Appellate Counsel",
        subheading=(
            "When a zoning decision, a contract, or a neighbor threatens your property, "
            "you need lawyers who try and win real property cases, not generalists "
            "learning as they go. Suder litigates only real property matters, and our "
            "results are published in Ohio's appellate reports."
        ),
        button="Discuss Your Case",
        description=(
            "Our lawyers have tried real property cases in Ohio's trial courts and won "
            "published appellate decisions on taxpayer standing, nonconforming uses, use "
            "variances, writs of mandamus, and spot zoning. Sean Suder served as lead "
            "trial counsel on the City of Cincinnati's land use and zoning cases for "
            "nearly four years, so we know how a municipality builds its case and how to "
            "take it apart. We resolve disputes efficiently when we can and try them when "
            "we must."
        ),
        bullets=[
            "Administrative appeals of zoning, planning, and building decisions (R.C. Chapter 2506)",
            "Writs of mandamus and declaratory judgment actions",
            "Temporary restraining orders and injunctions, including emergency orders to stop demolitions",
            "Civil rights claims involving property (42 U.S.C. Section 1983)",
            "Real estate contract disputes, misrepresentation, and fraud",
            "Appeals in Ohio's courts of appeals, including published decisions",
        ],
        results=[
            ("Taxpayer standing: Cincinnati ex rel. Miller v. Cincinnati, 2024-Ohio-4805 (1st Dist.)",
             "Representing the affordable housing developer (Over-the-Rhine Community "
             "Housing), Suder defeated a taxpayer suit attacking the City ordinance that "
             "approved the project; the First District vacated the judgment and ordered "
             "the case dismissed for lack of standing."),
            ("Nonconforming uses: Cook v. Lockland, 2024-Ohio-9 (1st Dist.)",
             "Representing a property owner against the Village of Lockland, Suder won a "
             "reversal holding that the village, not the owner, bears the burden of "
             "proving a nonconforming use was abandoned."),
            ("Use variances: Mt. Lookout Cmty. Council v. Cincinnati, 2023-Ohio-1729 (1st Dist.)",
             "Representing the neighborhood community council, Suder won a reversal "
             "vacating a use variance that would have allowed demolition of four "
             "buildings in Mt. Lookout; the court held demolition is not a land use that "
             "can be permitted through a use variance."),
            ("Emergency orders saving the Over-the-Rhine bell tower (2022-2023)",
             "J.P. Burleigh personally argued for and obtained multiple emergency court "
             "orders that stopped the demolition of a 150-year-old church bell tower on "
             "Washington Park. Strong story and visuals."),
            ("Additional published opinions for a longer list",
             "State ex rel. 506 Phelps Holdings, LLC v. Cincinnati Union Bethel, 2013-Ohio-388 "
             "(writ of mandamus); State ex rel. Phillips Supply Co. v. Cincinnati, 2012-Ohio-6096 "
             "(spot zoning; legislative variances); HillStreet Fund III, L.P. v. Bloom, "
             "2010-Ohio-2267 (2d Dist.) (summary judgment in foreclosure)."),
        ],
    ),
    # ------------------------------------------------------------------ 3
    dict(
        name="Real Estate Transactions",
        image_desc=(
            "Real project preferred: the downtown Cincinnati skyline at dusk featuring the "
            "18-story apartment tower above the downtown Kroger at Court and Walnut "
            "(Suder was lead transactional counsel on its sale-leaseback financing), or "
            "the former Millennium Hotel site across from the convention center. Stock "
            "fallback: a signed purchase agreement or lease on a conference table with "
            "building plans, or an aerial of a suburban retail center such as Kenwood "
            "Towne Centre (also a Suder matter). Avoid keys-in-hand residential cliches; "
            "this is commercial work."
        ),
        image_text="Counsel for the deal",
        heading="Big-Firm Deal Lawyers, Boutique Attention",
        subheading=(
            "Every deal turns on the details: what the land can actually be used for, what "
            "the lease really costs over twenty years, how the venture splits the upside "
            "when the financing shifts. Suder's transactional lawyers spent decades as "
            "partners at global and national firms, and now bring that experience to your "
            "acquisition, lease, joint venture, or financing without the big-firm overhead."
        ),
        button="Talk to a Deal Lawyer",
        description=(
            "Our transactional team combines two careers' worth of large-firm deal work. "
            "Sean Suder was a partner in the commercial real estate practices of two major "
            "Ohio firms and has closed nine-figure sale-leasebacks, hotel and tower "
            "acquisitions, and millions of square feet of retail, office, and industrial "
            "leases. Josh Bernstein, of counsel, spent more than twenty years at Skadden, "
            "Norton Rose Fulbright, Greenberg Traurig, and Armbrust & Brown, Austin's go-to "
            "firm for land use and development work, advising developers, investors, "
            "lenders, and operators on development-driven transactions (acquisitions, "
            "dispositions, and leasing) and on real estate finance and private equity "
            "(joint ventures, debt and equity financing, and fund formation) across every "
            "asset class, from single-family and multifamily to industrial, office, retail, "
            "and hotel, with particular depth in senior housing. He is a recognized "
            "authority on structuring complex condominiums for the financing and sale of "
            "commercial, residential, and mixed-use projects, including the W Austin Hotel "
            "& Residences and Austin's marquee master-planned communities. Because we also "
            "practice land use law every day, we catch the entitlement and zoning issues in "
            "a deal that purely transactional lawyers miss, and Sean is a licensed Ohio "
            "title agent."
        ),
        bullets=[
            "Acquisitions, dispositions, and financings across all asset classes: single-family and multifamily, office, retail, industrial, hospitality and timeshare, and senior and age-restricted housing",
            "Retail, office, industrial, and ground leasing for landlords and tenants",
            "Joint ventures, private equity and fund structures, and debt and equity financing for investors and operating partners",
            "Condominium formation and governance, including commercial and mixed-use condominium regimes, condominium structures as a density and land-planning tool, and master-planned communities",
            "Development agreements, covenants (CC&Rs), easements, licenses, and sale-leaseback and other financings",
            "Lender and borrower representation on commercial real estate loans, workouts, foreclosures, and distressed-asset resales; entity formation and M&A for real estate companies",
        ],
        results=[
            ("Grocery-anchored downtown tower (Cincinnati, 2018)",
             "Lead transactional counsel on the sale-leaseback financing for a new 18-story "
             "downtown apartment tower anchored by a multi-level Kroger store."),
            ("Convention hotel acquisition (Cincinnati, 2020)",
             "Lead transactional counsel on the acquisition of the 32-story Millennium Hotel "
             "across from the Duke Energy Convention Center."),
            ("$100 million assisted living portfolio (Ohio, Kentucky, and Indiana, 2020)",
             "Lead real estate counsel on the sale-leaseback financing of a multi-state "
             "assisted living portfolio."),
            ("Retail leasing program for a growing orthodontics group (2019)",
             "Lead leasing counsel for locations in the region's top retail centers, "
             "including Kenwood Towne Centre. Shows the tenant-side leasing work."),
            ("Playhouse Square residential tower (Cleveland, opened 2020)",
             "Counsel on a portion of the public financing for the 34-story apartment tower "
             "on Cleveland's historic Playhouse Square. Shows statewide reach."),
            ("W Austin Hotel & Residences condominium (Austin, Texas)",
             "Josh Bernstein prepared the condominium documents for the W Austin Hotel & "
             "Residences, the mixed-use tower combining a hotel, private residences, and "
             "commercial space, using the condominium regime to allocate ownership, "
             "control, and cost among very different uses in one building."),
            ("The Grove: 75 acres of state land into a walkable mixed-use community (Austin, Texas)",
             "Josh represented the private equity-backed developer in acquiring 75 acres of "
             "state-owned land in central Austin through a public bid process, including "
             "leaseback agreements with multiple state agencies, public procurement "
             "requirements, and affordable housing commitments, followed by the ongoing "
             "development, leasing, and parcel sales for the community."),
            ("Austin's marquee master-planned communities: Barton Creek and Mueller",
             "Josh was heavily involved in the development, condominium, and covenant "
             "work for several of the projects that shaped Austin's growth, including "
             "Barton Creek and the Mueller redevelopment. Good case study for large-scale "
             "community structuring."),
            ("Age-restricted master-planned communities structured as condominiums (Texas)",
             "For a master-planned community developer, Josh built a condominium structure "
             "for subdividing all of the land in multiple 55+ communities, unlocking "
             "significantly more density than a traditional platted subdivision would "
             "allow, and handled the sales of improved and unimproved parcels to "
             "sub-developers, homebuilders, and individuals. The best example of the "
             "\"condominium as land-planning tool\" concept. Client not to be named."),
            ("First-of-its-kind timeshare conversion for a national hospitality company",
             "Josh represented a national hospitality company in acquiring a Class A "
             "apartment building and converting it to timeshare use, securing a "
             "first-of-its-kind approval from local authorities, then structuring multiple "
             "condominium regimes to support a multi-club timeshare program and state "
             "timeshare registrations. Client not to be named."),
            ("Land acquisition program for a publicly traded homebuilder (Texas)",
             "Josh advised a public homebuilder on the simultaneous acquisition of dozens of "
             "unimproved parcels, negotiating entitlement and development agreements and "
             "utility and shared-facility agreements with sellers and neighbors, with a "
             "tracking system built to keep the volume on schedule. Client not to be named."),
            ("Joint venture for a major commercial and mixed-use project (San Diego, California)",
             "Josh represented an institutional developer in structuring and negotiating the "
             "joint venture for a large commercial and mixed-use development in San Diego. "
             "Client and project not to be named."),
            ("Commercial lender representation, including a distressed Houston project",
             "Josh has represented a commercial real estate lender across multiple loans "
             "nationwide, including a Houston development where the borrower's deal "
             "collapsed and the lender foreclosed and resold the asset. Shows the "
             "lender-side and workout capability. Client and projects not to be named."),
        ],
    ),
    # ------------------------------------------------------------------ 4
    dict(
        name="Eminent Domain & Takings",
        image_desc=(
            "Photo of private property on the edge of a public project: a commercial "
            "frontage or farm with orange survey stakes and flagging where a road widening "
            "or utility line is coming through, ideally in Ohio (an ODOT project is "
            "perfect). Alternative: a property owner standing at a fence line looking at "
            "construction equipment. Should feel like the owner's side, not the "
            "government's. Stock is fine here; the firm has no matter-specific photos it "
            "can publish for these clients."
        ),
        image_text="Counsel for the landowner",
        heading="Full Compensation When the Government Takes",
        subheading=(
            "The government arrives with its own appraisers and lawyers; you should have "
            "yours. Suder has represented more than 100 property owners in eminent domain "
            "and takings matters, and we know how to challenge a taking, contest a low "
            "appraisal, and recover what your property is actually worth."
        ),
        button="Protect Your Property",
        description=(
            "Teresa Bamberger has represented more than 100 clients in eminent domain and "
            "takings matters since 2011, and her earlier career as a certified planner and "
            "civil engineering project manager means she can read the plans, understand "
            "the damage to what is left of your property, and prove its real value. Our "
            "founder spent nearly four years as the City of Cincinnati's chief land use "
            "lawyer, so we also know how the condemning authority thinks. We handle both "
            "physical takings (appropriation and inverse condemnation) and regulatory "
            "takings, where a zoning or permitting decision goes so far that it takes your "
            "property without a formal appropriation."
        ),
        bullets=[
            "Appropriation (condemnation) defense and just compensation",
            "Challenges to necessity and public use",
            "Damages to the residue and partial takings",
            "Inverse condemnation",
            "Regulatory takings and related civil rights claims",
            "Highway, utility, pipeline, and redevelopment takings",
        ],
        results=[
            ("More than 100 owners represented in eminent domain and takings matters",
             FLAG + "Teresa Bamberger's track record since 2011. Sean/Teresa to pick two "
             "or three specific appropriations (for example, a highway widening where the "
             "award materially exceeded the initial offer) that can be described "
             "without client names."),
            ("Property rights against a municipality: Cook v. Lockland, 2024-Ohio-9 (1st Dist.)",
             "Representing the owner, Suder won a reversal holding the village must prove "
             "a nonconforming use was abandoned before it can strip the owner's vested "
             "right to continue it. Shows the firm's willingness to take a municipality "
             "to the court of appeals over property rights."),
            ("Regulatory takings / inverse condemnation matter",
             FLAG + "Suder lists regulatory takings and inverse condemnation among its "
             "litigation services; identify one representative matter (or a Section 1983 "
             "claim) that can be described generically."),
            ("Government-side perspective",
             "Sean Suder advised the City of Cincinnati on land use matters as Chief "
             "Counsel for Land Use and Planning (2010-2014). Can be framed on the results "
             "page as \"we know the playbook because we helped write it.\""),
        ],
    ),
    # ------------------------------------------------------------------ 5
    dict(
        name="Historic Preservation",
        image_desc=(
            "Real project photo, strongly preferred: the 150-year-old church bell tower "
            "on Washington Park in Over-the-Rhine that Suder saved from demolition in "
            "2022-2023 (Casey can shoot this; it is a public street view). Second choice: "
            "the Crosley Building in Camp Washington (adaptive reuse Suder entitled) or "
            "an Italianate streetscape in the Over-the-Rhine Historic District. Stock "
            "fallback: scaffolding on a restored 19th-century brick facade."
        ),
        image_text="Counsel for the places worth keeping",
        heading="Historic Preservation Counsel",
        subheading=(
            "Whether you are restoring a landmark, building in a historic district, or "
            "fighting to keep a building off the wrecking ball, the rules are technical "
            "and the deadlines are short. Sean Suder was lead counsel for Cincinnati's "
            "historic preservation ordinance, and we know how to use it."
        ),
        button="Get In Touch",
        description=(
            "As the City of Cincinnati's Chief Counsel for Land Use and Planning, Sean "
            "Suder served as lead counsel for the creation of the City's award-winning "
            "historic preservation ordinance and as counsel to the Historic Conservation "
            "Board. Since founding Suder, the firm has secured approvals for adaptive "
            "reuse and infill projects in historic districts and obtained emergency court "
            "orders that saved a 150-year-old bell tower in Over-the-Rhine from "
            "demolition. We handle certificates of appropriateness, landmark designations, "
            "preservation advocacy, and the zoning questions that come with historic "
            "property."
        ),
        bullets=[
            "Certificates of appropriateness before historic conservation and landmark boards",
            "Landmark and historic district designations (supporting or opposing)",
            "Adaptive reuse and infill approvals in historic districts",
            "Demolition permits, economic hardship claims, and emergency injunctions",
            "Preservation advocacy for neighborhoods and community councils",
            "Zoning and variance issues unique to historic buildings",
        ],
        results=[
            ("Saving the Washington Park bell tower (Over-the-Rhine, 2022-2023)",
             "Lead counsel in the successful effort to save the 150-year-old bell tower, "
             "including multiple emergency court orders J.P. Burleigh argued and won to "
             "halt demolition. The firm's signature preservation story."),
            ("Crosley Building adaptive reuse (Camp Washington, 2020-2021)",
             "Lead land use counsel for the $50 million conversion of the historic Crosley "
             "Radio Corp. headquarters into 175-250 apartments with artist housing."),
            ("Affordable senior housing in the historic urban core (Pendleton, 2026)",
             "Approval secured for an affordable senior housing project in one of "
             "Cincinnati's historic neighborhoods after the design was revised to respect "
             "its context. Shows the firm gets projects built in historic districts, not "
             "just blocked."),
            ("Blocking demolition in Mt. Lookout: Mt. Lookout Cmty. Council v. Cincinnati, 2023-Ohio-1729",
             "Representing the community council, Suder won a published First District "
             "decision vacating a use variance that would have allowed four buildings to "
             "be demolished. Shows the advocacy side of preservation."),
            ("Cincinnati's award-winning historic preservation ordinance",
             "Sean Suder was lead counsel for the ordinance's creation while at the City "
             "(2010-2014). Credential-style result rather than a client matter."),
        ],
    ),
    # ------------------------------------------------------------------ 6
    dict(
        name="Real Estate Taxation",
        image_desc=(
            "Photo of a Cincinnati commercial property that reads as \"value\": a "
            "mid-rise office or apartment building facade, or a mixed-use block in "
            "Over-the-Rhine or downtown. Alternative: an aerial of a suburban office park "
            "or industrial building. Stock fallback: a county property tax bill or "
            "valuation notice beside a calculator and building plans. Keep it "
            "commercial; no single-family homes."
        ),
        image_text="Counsel for the taxpayer",
        heading="Pay Tax on What Your Property Is Worth, Not More",
        subheading=(
            "An inflated valuation costs you every year until someone challenges it. "
            "Suder contests county valuations before boards of revision and the Ohio Board "
            "of Tax Appeals, and structures the abatements that make development pencil."
        ),
        button="Review My Valuation",
        description=(
            "Sean Suder took a lead role on real property tax appeals for the City of "
            "Cincinnati, so we have argued valuation from the government's side and know "
            "how to attack it from yours. Because we practice land use and real estate "
            "every day, we understand what actually drives value: entitlements, leases, "
            "condition, and the market. We handle valuation complaints and appeals, and we "
            "secure the real property tax abatements available for new construction and "
            "rehabilitation."
        ),
        bullets=[
            "Valuation complaints before county boards of revision",
            "Appeals to the Ohio Board of Tax Appeals and the courts",
            "Defense against school district and county-initiated increase complaints",
            "Real property tax abatements for new construction and renovation",
            "Tax exemption applications for qualifying properties",
            "Tax due diligence and allocation in acquisitions and development",
        ],
        results=[
            ("Commercial valuation reduction",
             FLAG + "No public example on the current site. Ideal: a board of revision or "
             "BTA matter where the firm cut an assessed value materially (state the "
             "percentage or dollar reduction without the client name)."),
            ("Tax abatement for a development project",
             FLAG + "Ideal: an abatement secured for a new-construction or rehab project, "
             "possibly one of the entitlement matters already on the results page "
             "(Crosley Building, Hyde Park Square)."),
            ("Real property tax appeals for the City of Cincinnati (2010-2014)",
             "Sean Suder took a lead role on the City's real property tax appeals as Chief "
             "Counsel for Land Use and Planning. Credential-style result."),
            ("Defense of a school-district increase complaint",
             FLAG + "If the firm has defended an owner against a board-of-education "
             "complaint seeking a higher value, that is a relatable example for owners."),
        ],
    ),
    # ------------------------------------------------------------------ 7
    dict(
        name="Local Counsel & Co-Counsel Services",
        image_desc=(
            "The John A. Roebling Suspension Bridge with the Cincinnati skyline behind it, "
            "shot from the Kentucky side. It shows both states the firm serves and reads "
            "as a bridge between out-of-town counsel and local knowledge. Alternative: "
            "the Suder conference room at 1502 Vine Street with a video call in progress. "
            "Avoid stock handshakes."
        ),
        image_text="Counsel for counsel",
        heading="Local Counsel and Co-Counsel for National Firms",
        subheading=(
            "When your client's matter lands in Ohio or Northern Kentucky, you need local "
            "counsel who knows the boards, the judges, and the codes, and who will make "
            "you look good rather than compete for your client. Suder is the go-to Ohio "
            "land use and real estate counsel for Am Law firms, including several Am Law "
            "25 and Am Law 50 firms, and our lawyers have sat on your side of the table."
        ),
        button="Engage Local Counsel",
        description=(
            "Suder serves as local counsel, co-counsel, and pro hac vice sponsor for "
            "national and regional law firms and their clients on zoning, land use, real "
            "estate, and property litigation matters across Ohio and Northern Kentucky, "
            f"where we have appeared in {NJ} jurisdictions. Our lawyers are "
            "licensed in Ohio, Kentucky, Texas, New York, and Washington, D.C., admitted "
            "in the federal courts in Ohio, and were partners at firms such as Norton "
            "Rose Fulbright, Greenberg Traurig, and Calfee, so we know exactly what "
            "outside counsel needs from local counsel: fast answers, clean work product, "
            "and no surprises. We also issue zoning opinion and verification letters for "
            "financings, provide expert witness services on land use matters, and can "
            "serve as Texas or New York transactional counsel through our of counsel Josh "
            "Bernstein."
        ),
        bullets=[
            "Local counsel for zoning hearings, administrative appeals, and litigation in Ohio and Northern Kentucky",
            "Pro hac vice sponsorship and support in Ohio state and federal courts",
            "Co-counsel on multi-state portfolio acquisitions, joint ventures, leases, and financings with Ohio, Kentucky, Texas, or New York components",
            "Zoning opinion and verification letters for lenders (Ohio, Kentucky, and D.C.)",
            "Expert witness and consulting services on zoning and land use; Texas condominium law consulting",
            f"Public records requests and entitlement due diligence in {NJ} jurisdictions",
        ],
        results=[
            ("Co-counsel to Am Law 25 and Am Law 50 firms",
             FLAG + "The firm describes itself as a go-to for several Am Law 25 and 50 "
             "firms. Pick one or two matters (firm names optional) that can be described "
             "generically, such as local zoning counsel on a national retailer's Ohio "
             "rollout or Ohio counsel on a multi-state portfolio."),
            ("Multi-state assisted living portfolio (Ohio, Kentucky, and Indiana, 2020)",
             "$100,000,000 sale-leaseback financing spanning three states; shows the firm "
             "handling the Ohio and Kentucky pieces of a portfolio deal."),
            ("Zoning verification and opinion letters for financings",
             FLAG + "The firm offers these in Ohio, Kentucky, and D.C. as an alternative "
             "to costly title-insurance zoning endorsements. A short example of a letter "
             "that unblocked a closing would work well here."),
            ("Statewide reach: Cleveland, Columbus, Toledo, Akron",
             f"Suder has represented clients in {NJ} Ohio and Northern Kentucky "
             "jurisdictions, including Cleveland's Playhouse Square tower financing and "
             "matters in Columbus, Toledo, Akron, and Westlake. Consider a map graphic "
             "built from the firm's jurisdictions list."),
            ("National deal experience: Texas, California, and beyond",
             "Through of counsel Josh Bernstein, the firm brings co-counsel-ready "
             "experience on institutional deals outside Ohio, including a joint venture for "
             "a major commercial and mixed-use project in San Diego, multiple loans for a "
             "national commercial lender, a first-of-its-kind timeshare conversion for a "
             "national hospitality company, and the condominium and community structures "
             "for the W Austin Hotel & Residences, Barton Creek, Mueller, and The Grove in "
             "Austin. Clients not to be named except as listed."),
        ],
    ),
]

# Firm-wide blocks the template references but does not give a slot for.
AWARDS = [
    "Chambers USA Spotlight Firm, Cincinnati Real Estate (2025, 2026)",
    "Chambers USA, Band 1, Ohio Real Estate: Zoning/Land Use, Sean S. Suder (2019-2026) " + FLAG.strip(),
    "The Best Lawyers in America, Real Estate Law and Land Use and Zoning Law, Sean S. Suder (2019-2025) " + FLAG.strip(),
    "Ohio Super Lawyers and Ohio Rising Stars, Sean S. Suder (2007, 2009, 2016-2018)",
]

CREDENTIALS = [
    "Attorneys licensed in Ohio, Kentucky, Texas, New York, and Washington, D.C.; admitted in the U.S. District Courts for the Southern and Northern Districts of Ohio; pro hac vice experience in Kentucky and West Virginia",
    "Former partners at Norton Rose Fulbright, Greenberg Traurig, Calfee, and Graydon (with training at Skadden and KMK); 23+ years of big-firm transactional experience through of counsel Josh Bernstein (development transactions, joint ventures, debt and equity financing, fund formation, M&A, condominium structuring, senior housing)",
    f"Zoning matters handled in {NJ} jurisdictions across Ohio and Northern Kentucky",
    "Active member, CREDA Cincinnati (the Commercial Real Estate Development Association serving Southwest Ohio and Northern Kentucky; NAIOP's local chapter) (Josh Bernstein)",
    "Founder served as the City of Cincinnati's Chief Counsel for Land Use and Planning (2010-2014)",
    "Adjunct Professor of Land Use and Development Law, University of Cincinnati College of Law",
    "Two AICP-certified planners on the team (Teresa Bamberger, Esq., AICP and Todd Kinskey, FAICP); founder holds a planning degree and LEED AP credential",
    "Licensed Ohio title agent on staff",
    "Member, APA Law & Planning Digest Advisory Board; creator and host of Zonecasts",
    "Sister firm ZoneCo (thezoneco.com) rewrites zoning codes for cities nationwide",
]

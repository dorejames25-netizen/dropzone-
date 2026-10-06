import random
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                PageBreak, NextPageTemplate, Table, TableStyle, KeepTogether)

W, H = A4
OUT = "Nightmare_Frequency_World_Guide.pdf"  # written next to where you run the script

INK = colors.HexColor("#0B090F")
SLATE = colors.HexColor("#112629")
TEAL = colors.HexColor("#1D4642")
MAG = colors.HexColor("#B03580")
GREEN = colors.HexColor("#2B7059")
NEON = colors.HexColor("#3DE689")
PAPER = colors.HexColor("#FAF8F4")
TEXT = colors.HexColor("#1B1A1F")
MUTED = colors.HexColor("#5B5963")
SAND = colors.HexColor("#C9A46A")
CARD = colors.HexColor("#EFEBE3")

# ---------- styles ----------
body = ParagraphStyle("body", fontName="Times-Roman", fontSize=11, leading=15.5, textColor=TEXT, spaceAfter=7)
small = ParagraphStyle("small", parent=body, fontSize=9.5, leading=13, textColor=MUTED, spaceAfter=4)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=SLATE, spaceBefore=0, spaceAfter=4)
kicker = ParagraphStyle("kicker", fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=MAG, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=SLATE, spaceBefore=10, spaceAfter=3)
bul = ParagraphStyle("bul", parent=body, leftIndent=14, bulletIndent=2, spaceAfter=3)
cell = ParagraphStyle("cell", fontName="Times-Roman", fontSize=10, leading=13, textColor=TEXT)
cellb = ParagraphStyle("cellb", parent=cell, fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=SLATE)
cellh = ParagraphStyle("cellh", parent=cell, fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=colors.white)
quote = ParagraphStyle("quote", parent=body, fontName="Times-Italic", fontSize=13, leading=18, textColor=SLATE, alignment=TA_LEFT)


def P(t, s=body):
    return Paragraph(t, s)


def B(items):
    return [Paragraph(t, bul, bulletText="•") for t in items]


def section(kick, title):
    return [P(kick.upper(), kicker), P(title, h1), rule(), Spacer(1, 6)]


def rule():
    t = Table([[""]], colWidths=[W - 40 * mm], rowHeights=[2])
    t.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -1), 1.6, MAG)]))
    return t


def callout(title, text):
    inner = [Paragraph("<b>%s</b>" % title, cellb), Spacer(1, 2), Paragraph(text, cell)]
    t = Table([[inner]], colWidths=[W - 40 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD),
        ("LINEBEFORE", (0, 0), (0, -1), 3, GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return [t, Spacer(1, 8)]


def grid(header, rows, widths):
    data = [[Paragraph(h, cellh) for h in header]]
    for r in rows:
        data.append([Paragraph(r[0], cellb)] + [Paragraph(c, cell) for c in r[1:]])
    t = Table(data, colWidths=widths, repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), SLATE),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
          ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
          ("LINEBELOW", (0, 1), (-1, -1), 0.4, colors.HexColor("#CFC9BC"))]
    for i in range(1, len(data)):
        if i % 2 == 0:
            st.append(("BACKGROUND", (0, i), (-1, i), CARD))
    t.setStyle(TableStyle(st))
    return [t, Spacer(1, 8)]


# ---------- cover ----------
def cover(c, doc):
    c.saveState()
    c.setFillColor(INK)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    random.seed(7)
    for _ in range(170):
        x, y = random.uniform(0, W), random.uniform(260, H)
        r = random.choice([0.4, 0.5, 0.7, 1.0])
        c.setFillColor(colors.HexColor(random.choice(["#8FB9A8", "#C9C2D6", "#6C8F86", "#D8298D"])))
        c.setFillAlpha(random.uniform(0.25, 0.8))
        c.circle(x, y, r, stroke=0, fill=1)
    c.setFillAlpha(1)
    # horizon + dunes
    c.setStrokeColor(NEON); c.setLineWidth(1.2); c.line(0, 255, W, 255)
    for col, base, amp in [("#3B2C1B", 255, 40), ("#5A4125", 215, 36), ("#8A6A3C", 165, 30)]:
        p = c.beginPath(); p.moveTo(-6, -6); p.lineTo(-6, base)
        p.curveTo(W * 0.22, base + amp, W * 0.38, base - amp * 0.6, W * 0.55, base + amp * 0.2)
        p.curveTo(W * 0.72, base + amp * 0.8, W * 0.88, base - amp * 0.5, W + 6, base + amp * 0.3)
        p.lineTo(W + 6, -6); p.close()
        c.setFillColor(colors.HexColor(col)); c.setStrokeColor(colors.HexColor("#0B090F")); c.setLineWidth(1.5)
        c.drawPath(p, stroke=1, fill=1)
    # title block
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(W / 2, 735, "NIGHTMARE FREQUENCY")
    c.setFillColor(NEON); c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(W / 2, 705, "S T O R Y   &   W O R L D   G U I D E")
    c.setFillColor(colors.HexColor("#C9C2D6")); c.setFont("Times-Italic", 14)
    c.drawCentredString(W / 2, 672, "History does not end. It repeats.")
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(W / 2, 40, "Working title  ·  Draft 2  ·  6 October 2026  ·  Prepared for James  ·  Dropzone project")
    c.restoreState()


def page(c, doc):
    c.saveState()
    c.setFillColor(PAPER); c.rect(0, 0, W, H, stroke=0, fill=1)
    c.setFillColor(MAG); c.rect(0, H - 8, W, 8, stroke=0, fill=1)
    c.setFillColor(NEON); c.rect(0, H - 8, 46, 8, stroke=0, fill=1)
    c.setFillColor(MUTED); c.setFont("Helvetica", 8)
    c.drawString(20 * mm, 12 * mm, "NIGHTMARE FREQUENCY  ·  Story & World Guide  ·  Draft 2 (working title)")
    c.drawRightString(W - 20 * mm, 12 * mm, "%d" % doc.page)
    c.restoreState()


doc = BaseDocTemplate(OUT, pagesize=A4, title="Nightmare Frequency - Story and World Guide (Draft 2)",
                      author="James (with Claude)", subject="Story and world guide, working title")
fr_c = Frame(20 * mm, 20 * mm, W - 40 * mm, H - 40 * mm, id="c")
fr_b = Frame(20 * mm, 20 * mm, W - 40 * mm, H - 40 * mm, id="b")
doc.addPageTemplates([PageTemplate(id="cover", frames=[fr_c], onPage=cover),
                      PageTemplate(id="body", frames=[fr_b], onPage=page)])

s = [NextPageTemplate("body"), PageBreak()]

# ---------- 1 pitch ----------
s += section("Section 1", "The pitch")
s += [P("Mankind has been owned for a very long time, and most of it never knew. A higher race, the Makers, built humans as a "
        "hybrid workforce in the age of the Ancients and have watched over the planet ever since. Earth turned out to be "
        "poorer in gold than they hoped, so they never left and never let go.")]
s += [P("When humans put up satellites, the Makers found a door into our own network. When humans built the first AI, bionic "
        "upgrades and virtual cyber centres, they sent something through it: a data virus called the <b>Nightmare Frequency</b>. "
        "It controls bionic upgrades and the human mind, and it warps virtual reality into reality. In a single day it took "
        "control of everything. The public still does not know.", body)]
s += [P("<i>Nightmare Frequency</i> is a comic-noir adventure set inside a cyberpunk-gothic future. You are part of "
        "<b>Project Nightmare Frequency</b>, a black-ops team of scientists and a secretly funded world organisation, trying "
        "to stop it before it takes the last people who are still free.")]
s += [Spacer(1, 4), P("“History does not end. It repeats.”", quote), Spacer(1, 6)]
s += [P("The core in five lines", h2)]
s += B(["<b>Tone:</b> gothic noir inside a cyberpunk city. Heavy shadow, silhouettes, rain-slick neon, cathedral architecture.",
        "<b>Threat:</b> the Nightmare Frequency. Glowing code, glitching grinning faces and reality that will not hold still.",
        "<b>Supreme being:</b> the Creator of Stars and Worlds. Never shown, only felt and evidenced, never explained.",
        "<b>Demigods:</b> entities lost in time, trapped inside the Tower of Tongues data centre.",
        "<b>Game:</b> a fixed-camera adventure with high-detail still backgrounds and a bold comic look."])
s += callout("Reading used in this draft",
             "Your notes now describe two ages, so I have joined them like this. <b>Age one</b>: the Makers made humans, a first "
             "great civilisation built the Tower, and an extinction event destroyed it. The elite (the Sleepers) fled on the ark "
             "into a virtual sleep and everyone else was left behind. <b>Age two (now)</b>: mankind rebuilt, history repeated, and "
             "the Makers used the new satellites to strike. If any link is wrong, tell me and I will change it.")
s.append(PageBreak())

# ---------- 2 timeline ----------
s += section("Section 2", "The cycle: a timeline")
s += [P("In this world, time itself is called <b>Aion</b>. Things happened <i>aions ago</i>, and the ages below are the turning of Aion. "
        "Each age repeats the one before it, and every one ends with someone left behind.")]

s += grid(["Age", "What happened", "What it left behind"], [
    ["The Creator", "Before stars and worlds. The Creator of Stars and Worlds makes the heavens and everything in them.",
     "A silence that every later age tries to fill."],
    ["Age of the Ancients", "The Three Spirits take their places over the aions. The Ancients, the first great peoples, rise "
                            "and their lore, glyphs and names are carved into the world. Two of those peoples go to war.",
     "Ancient glyphs, carved myths and the Spirits’ marks, still readable."],
    ["Age of Makers", "The Makers find Earth and make a hybrid slave race to work it. Humans are controlled from the age of the "
                      "Ancients onward. Pyramids rise in the four corners of the world and serve as beacons.",
     "Humanity: made, not born, and made to serve. Beacons that still stand."],
    ["Poor Ground", "Earth proves too poor in gold to be worth settling. The Makers keep a thin watch and keep humans as a workforce.",
     "A watching presence that never fully leaves."],
    ["Rise of Man (age one)", "Humans build cities and, at last, the Tower: a great data centre to hold everything they know.",
     "The Tower of Tongues. Knowledge without anyone left who can read it."],
    ["The Wiping", "An extinction event destroys the Tower and almost all of mankind. Its cause is deliberately left open in this draft.",
     "Ruins, ash and a very small number of survivors."],
    ["The Ark and the Sleep", "Only the rich and important are chosen: scientists and the elite. Their minds are frozen into a "
                              "virtual world while the ship searches for a new planet.",
     "A neon, gothic city that never sleeps, full of people who never wake."],
    ["The Long Dark", "Everyone else is left behind and falls back into the Stone Age over aions, with fire, bone tools, cave paintings and stories.",
     "A people who remember the gods only as myth."],
    ["Rise of Man (age two)", "Humans rebuild. The first satellites and space stations replace the old beacons.",
     "A new network, and a new door."],
    ["The Link", "The Makers connect through the satellites and watch how fast humans are evolving: first AI, bionic upgrades, virtual cyber centres.",
     "Humans who do not know they are being watched."],
    ["The Nightmare Frequency", "The Makers infect the cyber centres with a virus that controls bionic upgrades and the human mind. "
                                "In one day they take control of everything.",
     "Insanity, violence, and a public that does not know. Many high officials already controlled."],
    ["The Present", "Scientists and world leaders who know form Project Nightmare Frequency, a black-ops team with special world funding.",
     "The game begins here."],
], [34 * mm, 84 * mm, 52 * mm])
s.append(PageBreak())

# ---------- 3 the frequency ----------
s += section("Section 3", "The Nightmare Frequency and the Project")
s += [P("The virus", h2)]
s += [P("A data virus built by the Makers and carried through the satellite link into every cyber centre. It does three things: "
        "it takes control of bionic upgrades, it takes control of the human mind, and it warps virtual reality into reality. "
        "Most people it touches go insane or harm others. In one day it was everywhere.")]
s += grid(["Effect", "What the player sees", "How we show it"], [
    ["Reality bleed", "Virtual things appearing in the real world", "Glitch shader, doubled outlines, scene colours flickering"],
    ["Controlled people", "Officials and citizens with upgrades, acting as one", "Eyes lit magenta, stiff movement, shared pauses"],
    ["The grin", "A face that smiles inside screens and walls", "Glitching grin on dashboards, posters and the skyline"],
    ["The rain", "Falling glyphs, emoji and numbers", "Looping animation over screens and sky"],
], [30 * mm, 66 * mm, 74 * mm])
s += [P("Project Nightmare Frequency", h2)]
s += [P("A black-ops team led by scientists and backed by a specially funded world organisation. Its members are the few "
        "people at the top who know what is happening and have not been taken. Many high officials already have been, "
        "so the Project works in secret, answers to no public body, and cannot tell who is safe to trust.")]
s += B(["<b>Why it exists:</b> to find the source, cut the link and stop the infection before it reaches everyone.",
        "<b>Who is in it:</b> scientists, engineers, a handful of loyal leaders, and the people they recruit.",
        "<b>Threat inside the walls:</b> anyone with an upgrade could be controlled. Trust is a game mechanic."])
s += callout("The ancient glyph look",
             "The falling code uses carved glyph styles from ancient civilisations, plus emoji and numbers. This is history used as "
             "a visual language, not a faith, and the glyphs stay separate from real living religious symbols.")
s.append(PageBreak())

# ---------- 4 two worlds ----------
s += section("Section 4", "Two worlds")
s += [P("The game moves between a world that is too bright and a world that is too bare.")]
s += [P("The Sleep (inside)", h2)]
s += [P("A cyberpunk city built by sleeping minds, with gothic noir bones: cathedral arches, long galleries, wine cellars, mansions "
        "full of locked rooms, corridors that run on forever. Every room is lit by one colour, and that colour tells the player "
        "who is in charge there. Your Sanctum mansion map lives here. Its Cyber Room / Mainframe boss is the part of the Tower "
        "that reaches into the city.")]
s += [P("The Sands (outside)", h2)]
s += [P("A hard, warm, Stone Age world. Sand and ochre, bone, fire, hand-painted walls, huge ruins half-buried. The Tower stands on "
        "the horizon, the one thing still glowing. Few words, few colours, a lot of silence. This is the narrator’s home, as in "
        "<i>Sands of Time</i>, where the desert itself does the telling.")]
s += grid(["", "The Sleep", "The Sands"], [
    ["Light", "Neon: one key colour per room, hard shadows", "Fire and sun: warm, low, honest"],
    ["Materials", "Marble, glass, wet stone, brass, screens", "Sand, bone, clay, hide, ash"],
    ["Sound", "Hum, rain, distant music, static", "Wind, fire, breath, drums"],
    ["Feeling", "Beautiful, decaying, watched", "Hungry, hard, free"],
], [24 * mm, 73 * mm, 73 * mm])
s += callout("Why the contrast matters",
             "The Sleepers have all the light and none of the life. The Left Behind have all the life and none of the light. "
             "Every room the player enters should make one of those two things obvious.")
s.append(PageBreak())

# ---------- 4 powers ----------
s += section("Section 5", "The Creator and the Lost")
s += [P("The Creator of Stars and Worlds", h2)]
s += [P("The supreme being of the story. The Creator is never seen and never speaks. The player finds <i>evidence</i>: a sky that "
        "does not match the maps, a signal beneath the data, a pattern in the sand. The story never explains the Creator. "
        "It makes sure the characters are always acting in its sight.")]
s += [P("Aion (time)", h2)]
s += [P("Aion is time as a living force: older than the Spirits and answerable only to the Creator. Characters say "
        "“aions ago” for the deep past, and the Tower’s clocks are all set to Aion. Aion is a force, not a being: it cannot be "
        "bargained with, only endured, spent or turned.")]
s += [P("The Ancients and the Three Spirits", h2)]
s += [P("This is the oldest layer of lore, taken from <i>Sands of Time</i>. Over the aions the Creator’s will is carried by three "
        "great Spirits: one of <b>light</b>, one of <b>shadow</b> and one of <b>balance</b>. Beneath them stand six lesser "
        "powers. The Ancients, the first great peoples, told their stories and carved their glyphs under the Spirits’ marks. "
        "Two of those peoples, one druidic and one from the desert empires, went to war over who the Spirits favoured. "
        "That war is why so much ancient writing survives: each side carved its version into stone.")]
s += B(["<b>Where the player meets it:</b> glyph walls, carved murals, the falling-code rain and monuments beneath the Tower.",
        "<b>Why it matters now:</b> the Makers hid inside the Ancients’ stories, and the Nightmare Frequency’s glyphs are the Ancients’ own marks, twisted by the virus."])
s += [P("The Lost (the demigods)", h2)]
s += [P("Entities that have been lost in time. Some are remnants of the Makers, some are fragments of the Spirits and the lesser "
        "powers remembered by the Ancients and the Left Behind, and some are pieces of the Tower’s own mind that became more than "
        "a program. Each one is trapped on a floor of the Tower. The six below are draft archetypes that we will match to the "
        "six lesser powers when the full codex is merged in.")]
s += grid(["Working name", "What they are", "What they want"], [
    ["The Archivist", "Keeper of every name ever recorded; has forgotten its own.", "To be named."],
    ["The Ferryman", "Carries minds between the Sleep and the Sands.", "A passenger who will not be forgotten."],
    ["The Weaver", "Rewrites history inside the Tower so that nothing ever repeats the way it really did.", "A perfect, unchanging past."],
    ["The Warden", "Guards the Tower gates. Loyal to the Sleepers because it was told to be.", "An order that can finally be refused."],
    ["The Mirror", "Copies anyone who stands before it, memory and all.", "A self of its own."],
    ["The Hollow", "A god that forgot what it was a god of.", "To remember, or to be ended."],
], [34 * mm, 80 * mm, 56 * mm])
s.append(PageBreak())

# ---------- 5 tower ----------
s += section("Section 6", "The Tower of Tongues data centre")
s += [P("The Tower is both the machine that holds the Sleep together and the one place where the two worlds touch. It was built to "
        "keep every language alive. Over the aions the Sleep has slowly lost the ability to read them, and the name stuck: "
        "the Tower of Tongues.")]
s += grid(["Level", "Role in the story", "Look"], [
    ["Roots (the Sands)", "Entrance. Left Behind pilgrims leave offerings at the base.", "Sandstone, rope, hand-painted symbols, a single glowing door."],
    ["The Cellars", "Power, cooling, the old servers. Where the Lost are first met.", "Dark brick, wet stone, rows of humming racks."],
    ["The Archive Floors", "Every language ever spoken, stored but unreadable.", "Endless shelves, glass cases, whispering screens."],
    ["The Court", "Where the Sleepers’ council rules the city by committee.", "Marble, red leather, long tables, too many chairs."],
    ["The Crown", "The top. Where the Creator’s signal can be heard.", "Light with no source, a sky that is not a sky."],
], [34 * mm, 72 * mm, 64 * mm])
s += [P("How it links to the mansion", h2)]
s += [P("The Sanctum map already has a Cyber Room / Mainframe and a Security / CCTV room. In this world they become a branch of "
        "the Tower: the first place the player sees the Tower’s mind watching them. The Wine Room and the locked cellars match "
        "the Tower’s Cellars level.")]
s.append(PageBreak())

# ---------- 6 factions ----------
s += section("Section 7", "Peoples and factions")
s += grid(["Faction", "Who they are", "What they believe"], [
    ["The Makers", "The elite race who made humankind as workers and have watched Earth ever since. They sent the virus.",
     "Creation is ownership."],
    ["Project Nightmare Frequency", "A black-ops team of scientists and a secretly funded world organisation.",
     "Humans must be free, and the Makers can be stopped."],
    ["The Controlled", "Officials and citizens taken by the virus through bionic upgrades.",
     "Nothing of their own. They move as one."],
    ["The Sleepers", "Humanity’s rich and important: scientists and the elite, frozen in the virtual world.",
     "They saved the best of mankind, so they were right to leave the rest."],
    ["The Left Behind", "Descendants of everyone not chosen. Stone Age tribes, storytellers, hunters and diggers.",
     "The gods left, but the sky is still watching."],
    ["The Lost", "The demigods trapped in the Tower.", "Different for each one. See Section 4."],
    ["The Wardens", "The Tower’s machine guards, loyal to the Sleepers by default.",
     "Order must be kept, even when nobody remembers why."],
], [32 * mm, 75 * mm, 63 * mm])
s += [P("The player character (open choice)", h2)]
s += B(["<b>A Left Behind who climbs the Tower</b> (recommended): the story is about the abandoned reaching the people who abandoned them.",
        "<b>A Sleeper who wakes up early:</b> the story is about a privileged person discovering what the privilege cost.",
        "<b>A Lost entity in a borrowed body:</b> a demigod finds a way back, and the player finds out who it was."])
s += [P("Whichever we choose, we should also keep one companion on the other side, so the two worlds always have a voice in the room.")]
s.append(PageBreak())

# ---------- 7 voice & look ----------
s += section("Section 8", "Voice, tone and look")
s += [P("Narrative voice", h2)]
s += B(["Mythic and ceremonial, with a touch of clinical, cosmic precision, as in <i>Sands of Time</i>.",
        "The sand or desert as the narrator, always slightly amused and always patient.",
        "The divine is felt and unseen: evidenced, not explained.",
        "Cultures are represented equally and respectfully. Myths are inspiration, not claims. No real modern figures as characters."])
s += [P("Visual direction", h2)]
s += B(["<b>Comic-noir:</b> bold shapes, hard shadow steps, heavy ink, high contrast, one key colour per room.",
        "<b>Fixed-camera stills:</b> high-detail backgrounds with furniture and objects painted in.",
        "<b>The Sleep:</b> deep teal and near-black with neon green and magenta, like the hallway and nightclub reference frames.",
        "<b>The Sands:</b> ochre, bone, charcoal and fire-orange, with the Tower as the only neon on the horizon.",
        "<b>Real 3D feeling from flat pictures:</b> invisible boundaries around objects, depth layers to walk behind, and gentle "
        "animation in the background."])
s += grid(["Reference", "What we take from it"], [
    ["Lit hallway frame (green / magenta)", "Painted texture, coloured light, ink outlines, silhouettes"],
    ["Cyber nightclub set (bar, floor, DJ stage, VIP corridor)", "Layouts and neon colour mixes for the Sleep"],
    ["Long Gallery benchmark and stair hall", "Flat comic base and strong perspective"],
    ["Sanctum mansion map", "Room list, floors and connections"],
    ["Sands of Time codex", "Mythology, voice, deities, weapons index"],
], [75 * mm, 95 * mm])
s.append(PageBreak())

# ---------- 8 game plan ----------
s += section("Section 9", "How the game is built")
s += [P("The game is a separate build from the one Codex is working on. Codex helps with code and with 3D room models on the side. "
        "Nothing here depends on the old project.")]
s += grid(["Phase", "What gets done", "What waits"], [
    ["1. Placeholder scene", "One high-detail still background from Firefly. Walk boundaries around objects, depth layers, "
                             "animated background parts. Art locked.", "Sprites, lighting, graphics, player."],
    ["2. Player and camera", "A simple player, camera cuts between scenes, door triggers, basic click-and-point.", "Story scenes."],
    ["3. Light and effects", "Coloured lighting, fog, glow, background animation polish.", "More rooms."],
    ["4. Rooms and story", "Room by room, following the mansion map and the Tower levels.", "Extra content."],
], [34 * mm, 90 * mm, 46 * mm])
s += [P("Suggested folders for the new <b>dropzone</b> repo", h2)]
s += B(["<b>story/</b> this guide and the Sands of Time codex",
        "<b>art/references/</b> benchmarks, nightclub frames, lit hallway frame, mansion map",
        "<b>art/backgrounds/</b> final stills, one folder per room",
        "<b>art/sprites/</b> creatures and characters, later",
        "<b>third-party/</b> third-party asset packs (such as the mansion pack), with their licence files kept beside them",
        "<b>godot/</b> the game project",
        "<b>docs/</b> style rules, scene notes, handoff notes"])
s += callout("Keep the repo light",
             "Original art files can be very large. Keep only finished stills in the repo and leave raw Firefly exports in "
             "a folder outside it, or add Git LFS before the first big push.")
s.append(PageBreak())

# ---------- 9 open ----------
s += section("Section 10", "Open decisions and next steps")
s += [P("Questions to settle")]
s += B(["What caused the Wiping, or does the game never say?",
        "Are the Sleepers still out there on the ark, and do they know about the virus?",
        "Where is the new Tower, and is the Nightmare Frequency broadcast from it?",
        "Can the Makers be beaten, or only held back?",
        "Who is the player: a Left Behind, a Sleeper, or a Lost entity?",
        "What does the Sleep still need from the Left Behind? A reason for the Tower to call down to the Sands.",
        "Do the Makers get a name of their own, or one from <i>Sands of Time</i>?",
        "What do we call the Three Spirits and the two warring peoples in this game? Original names are needed.",
        "Single player only, or two-player co-op later?",
        "Final title. “The Left Behind” is a working placeholder.",
        "What is the ending: wake the Sleepers, leave them sleeping, or reach the Creator?"])
s += [P("Next steps", h2)]
s += B(["Drop the full <i>Sands of Time</i> codex into the story folder so I can merge the deities and voice into this guide.",
        "Create the <b>dropzone</b> repo under the dorejames25-netizen account and tell me its name.",
        "Pick the first scene for the placeholder (the Metro platform is now the lead candidate).",
        "I write the Firefly prompt for that scene, using the bold comic style and the key colour for the room."])
s += callout("Naming and legal rules",
             "Use original names for people, places, gods and groups. Take themes from old stories, never their exact names or "
             "texts. Do not copy brands, game or film titles, logos or characters. Never mock or offend a faith or culture. "
             "If a real name seems useful, check it first and leave it out unless it is clearly free to use. Keep licence "
             "files with every third-party asset.")
s += [P("Influences", h2)]
s += [P("Ancient tales of made servants and fallen builders (kept original), cyberpunk and film noir, fixed-camera adventure "
        "games, bold graphic comic art, and your own <i>Sands of Time</i> notes. We take themes and feelings, never names.", small)]

doc.build(s)
print("built", OUT)

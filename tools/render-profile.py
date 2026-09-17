from pathlib import Path
P={
'A':["01110","10001","10001","11111","10001","10001","10001"],
'B':["11110","10001","10001","11110","10001","10001","11110"],
'C':["01111","10000","10000","10000","10000","10000","01111"],
'D':["11110","10001","10001","10001","10001","10001","11110"],
'E':["11111","10000","10000","11110","10000","10000","11111"],
'F':["11111","10000","10000","11110","10000","10000","10000"],
'G':["01111","10000","10000","10111","10001","10001","01111"],
'H':["10001","10001","10001","11111","10001","10001","10001"],
'I':["11111","00100","00100","00100","00100","00100","11111"],
'J':["00111","00010","00010","00010","10010","10010","01100"],
'K':["10001","10010","10100","11000","10100","10010","10001"],
'L':["10000","10000","10000","10000","10000","10000","11111"],
'M':["10001","11011","10101","10101","10001","10001","10001"],
'N':["10001","11001","10101","10011","10001","10001","10001"],
'O':["01110","10001","10001","10001","10001","10001","01110"],
'P':["11110","10001","10001","11110","10000","10000","10000"],
'R':["11110","10001","10001","11110","10100","10010","10001"],
'S':["01111","10000","10000","01110","00001","00001","11110"],
'T':["11111","00100","00100","00100","00100","00100","00100"],
'U':["10001","10001","10001","10001","10001","10001","01110"],
'V':["10001","10001","10001","10001","10001","01010","00100"],
'W':["10001","10001","10001","10101","10101","11011","10001"],
'X':["10001","10001","01010","00100","01010","10001","10001"],
'Y':["10001","10001","01010","00100","00100","00100","00100"],
'Z':["11111","00001","00010","00100","01000","10000","11111"],
'0':["01110","10001","10011","10101","11001","10001","01110"],
'1':["00100","01100","00100","00100","00100","00100","01110"],
'2':["01110","10001","00001","00010","00100","01000","11111"],
'3':["11110","00001","00001","01110","00001","00001","11110"],
'4':["00010","00110","01010","10010","11111","00010","00010"],
'5':["11111","10000","10000","11110","00001","00001","11110"],
'6':["01110","10000","10000","11110","10001","10001","01110"],
'7':["11111","00001","00010","00100","01000","01000","01000"],
'8':["01110","10001","10001","01110","10001","10001","01110"],
'9':["01110","10001","10001","01111","00001","00001","01110"],
'/' : ["00001","00010","00010","00100","01000","01000","10000"],
'.' : ["00000","00000","00000","00000","00000","01100","01100"],
'-' : ["00000","00000","00000","11111","00000","00000","00000"],
'_' : ["00000","00000","00000","00000","00000","00000","11111"],
}

def gid(c): return 'g'+format(ord(c),'x')
def pd(p):
    out=[]
    for y,row in enumerate(p):
        for x,v in enumerate(row):
            if v=='1': out.append(f'M{x} {y}h1v1h-1z')
    return ''.join(out)

def line(text,x,y,s,color,center=False):
    w=sum((4.2 if c==' ' else 6.8) for c in text)*s
    xx=x-w/2 if center else x
    out=[f'<g transform="translate({xx:g} {y:g}) scale({s:g})" fill="{color}">']
    cur=0
    for c in text:
        if c==' ': cur+=4.2; continue
        out.append(f'<use href="#{gid(c)}" x="{cur:g}"/>'); cur+=6.8
    out.append('</g>'); return ''.join(out)

lines=[
('RIMM',700,210,14,'#F0FDF4',True),
('WEB DEVELOPER / FULL STACK',700,258,2.9,'#A7F3D0',True),
('UI UX / GAME SYSTEMS / DATA',700,292,2.25,'#D1FAE5',True),
('INDONESIA / TKJ / IT',700,322,1.9,'#86EFAC',True),
('01 / ABOUT',110,515,2.8,'#A3E635',False),
('BUILD / SHIP / GROW',110,558,4.8,'#F0FDF4',False),
('DEVELOPER / TKJ / NETWORKING / IT',110,600,1.95,'#B7E4C7',False),
('INTERFACE / ARCHITECTURE / DATABASE',110,635,1.95,'#B7E4C7',False),
('02 / STACK',110,865,2.8,'#A3E635',False),
('TOOLS I BUILD WITH',110,908,4.8,'#F0FDF4',False),
('TYPESCRIPT / REACT / NEXT JS',110,952,1.85,'#D1FAE5',False),
('SUPABASE / POSTGRES / DOCKER',110,986,1.85,'#D1FAE5',False),
('03 / PROJECTS',110,1208,2.8,'#A3E635',False),
('RIMMPAGE',140,1252,2.7,'#D9F99D',False),
('GAMING PLATFORM / PROGRESSION',140,1285,1.7,'#B7E4C7',False),
('AUTOMATION',740,1252,2.7,'#D9F99D',False),
('BOTS / APIS / SCRIPTS / TOOLS',740,1285,1.7,'#B7E4C7',False),
('WEB EXPERIENCES',140,1450,2.7,'#D9F99D',False),
('RESPONSIVE UI / UX / DASHBOARDS',140,1483,1.65,'#B7E4C7',False),
('EXPERIMENTS',740,1450,2.7,'#D9F99D',False),
('PROTOTYPE / BREAK / LEARN',740,1483,1.65,'#B7E4C7',False),
('04 / ENGINEERING',110,1695,2.8,'#A3E635',False),
('TRACE THE ROOT CAUSE',110,1738,4.8,'#F0FDF4',False),
('DATABASE / RPC / RLS / CONCURRENCY',110,1782,1.75,'#B7E4C7',False),
('SERVER LOGIC / VALIDATION / DATA',110,1815,1.75,'#B7E4C7',False),
('VERIFY / FIX / ITERATE',110,1848,1.95,'#D9F99D',False),
('05 / PROFILE',110,2115,2.8,'#A3E635',False),
('BUILD WITH INTENT',700,2162,5.2,'#F0FDF4',True),
('MAKE THE INTERFACE FEEL ALIVE',700,2202,1.8,'#B7E4C7',True),
('KEEP THE LOGIC HONEST',700,2235,1.8,'#B7E4C7',True),
('GITHUB COM / RIMMALFAREZI',700,2285,1.7,'#86EFAC',True),
('FOREST DIGITAL ONLINE',700,2318,1.65,'#6FA98A',True),
]
used=set(c for t,*_ in lines for c in t if c!=' ')
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="2400" viewBox="0 0 1400 2400"><defs>']
parts.extend(f'<path id="{gid(c)}" d="{pd(P[c])}"/>' for c in sorted(used))
parts.append('<linearGradient id="b" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#020805"/><stop offset=".38" stop-color="#06180F"/><stop offset=".75" stop-color="#092317"/><stop offset="1" stop-color="#010403"/></linearGradient><linearGradient id="p" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0A2417"/><stop offset="1" stop-color="#031009"/></linearGradient><linearGradient id="l" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#F0FDF4"/><stop offset=".5" stop-color="#A3E635"/><stop offset="1" stop-color="#16A34A"/></linearGradient><radialGradient id="m"><stop stop-color="#E9FAD9" stop-opacity=".25"/><stop offset="1" stop-color="#E9FAD9" stop-opacity="0"/></radialGradient></defs>')
parts.append('<rect width="1400" height="2400" rx="34" fill="url(#b)"/><circle cx="1080" cy="220" r="450" fill="url(#m)"/><circle cx="1080" cy="220" r="72" fill="#EFFFE0" opacity=".92"/><circle cx="1108" cy="194" r="72" fill="#04110A"/>')
parts.append('<path d="M0 470L80 340L150 440L230 305L310 440L390 325L470 450L550 295L635 440L715 310L800 452L880 322L965 445L1040 300L1125 450L1210 320L1290 445L1380 315L1400 340V910H0Z" fill="#04120B"/><path d="M0 680L92 540L170 645L255 515L340 650L430 535L515 660L605 520L690 650L780 500L870 650L960 540L1045 665L1130 520L1215 650L1300 540L1400 650V1040H0Z" fill="#0A2115"/><path d="M0 850C200 735 350 900 540 815C730 730 920 900 1090 815C1225 750 1320 795 1400 750V1080H0Z" fill="#020A05"/>')
for x,y,s,r in [(120,150,1,15),(300,350,.7,-25),(520,460,1.05,-12),(925,345,.8,20),(1195,500,.95,-18),(1280,720,.72,12),(160,900,.8,-18),(1070,900,.9,22),(125,1350,.82,10),(1230,1430,1,-25),(280,1880,.75,14),(1110,1880,.9,-15),(150,2140,.8,18),(1260,2170,.95,-10)]:
    parts.append(f'<g transform="translate({x} {y}) rotate({r}) scale({s})"><path d="M0 0C9-14 25-10 28 3C30 17 17 30 2 39C4 23 2 9 0 0Z" fill="url(#l)"/><path d="M5 30L23 8" stroke="#14532D" stroke-width="1.8"/></g>')
for y,h in [(105,330),(455,330),(805,350),(1145,650),(1870,370),(2080,260)]:
    parts.append(f'<rect x="70" y="{y}" width="1260" height="{h}" rx="28" fill="url(#p)" stroke="#4ADE80" stroke-opacity=".18"/>')
for row in lines: parts.append(line(*row))
parts.append('<rect x="70" y="2360" width="1260" height="2" fill="#4ADE80" fill-opacity=".15"/><rect x="2" y="2" width="1396" height="2396" rx="32" fill="none" stroke="#174D32" stroke-width="3"/></svg>')
Path('assets/profile-forest.svg').write_text(''.join(parts))
print(len(Path('assets/profile-forest.svg').read_text()))

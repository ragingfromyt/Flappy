import struct,zlib
from pathlib import Path
def make(n):
    rows=[]
    bird=[
    "..........KKKKKK........",
    ".......KKKYYYYWWKK......",
    ".....KKYYYYYYWWWWWK.....",
    "....KYYYYYYYYWWKWWK.....",
    "...KYYYYYYYYYWWKWWK.....",
    "..KYYYYYYYYYYWWWWWK.....",
    ".KKKKKKYYYYYYYKKKKKKKK..",
    "KWWWWWWKYYYYKKRRRRRRRRK.",
    "KWWWWWWWKYYYKRRRRRRRRRRK",
    ".KWWWWWKYYYYKKKKKKKKKKK.",
    "..KKKKKYYYYYKKRRRRRRK...",
    "...KYYYYOOYYYKKKKKKK....",
    "....KKOOOOOOKK..........",
    "......KKKKKK............"]
    colors={'K':(61,43,38),'Y':(255,215,48),'W':(255,250,225),'R':(235,70,49),'O':(244,149,38)}
    for y in range(n):
        row=bytearray()
        for x in range(n):
            a,b=x*48//n,y*48//n
            col=(126,194,204)
            if b>=39: col=(222,216,145)
            elif b>=36: col=(116,188,51) if (a+b)%5<3 else (166,220,80)
            elif b>=30: col=(187,231,174)
            if 12<=a<36 and 15<=b<29: col=colors.get(bird[b-15][a-12],col)
            row.extend(col)
        rows.append(b'\0'+row)
    def chunk(t,d):return struct.pack('>I',len(d))+t+d+struct.pack('>I',zlib.crc32(t+d)&0xffffffff)
    return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',n,n,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(rows),9))+chunk(b'IEND',b'')
if __name__=='__main__':
    import sys
    p=Path(sys.argv[1]);p.mkdir(parents=True,exist_ok=True)
    for n in (120,180,192,512,1024): (p/f'icon-{n}.png').write_bytes(make(n))

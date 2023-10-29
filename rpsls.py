import sys
for i in sys.argv[1:]:
    x=set(i)
    if x==set(('✂','📄')):y='✂ cuts 📄'
    if x==set(('💎','📄')):y='📄 covers 💎'
    if x==set(('💎','🦎')):y='💎 crushes 🦎'
    if x==set(('🖖','🦎')):y='🦎 poisons 🖖'
    if x==set(('🖖','✂')):y='🖖 smashes ✂'
    if x==set(('🦎','✂')):y='✂ decapitates 🦎'
    if x==set(('🦎','📄')):y='🦎 eats 📄'
    if x==set(('🖖','📄')):y='📄 disproves 🖖'
    if x==set(('🖖','💎')):y='🖖 vaporizes 💎'
    if x==set(('✂','💎')):y='💎 crushes ✂'
    if len(x)==1:y='Tie'
    print(y)
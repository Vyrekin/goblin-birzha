import base64
s=open('src.html',encoding='utf-8').read()
for k,f in (('__BG__','bg.jpg'),('__HERO__','hero.jpg'),('__GOB__','gob.jpg'),('__HERO2__','hero2.jpg'),('__HERO3__','hero3.jpg')):
    s=s.replace(k,'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode())
s=s.replace('__CHART__',open('node_modules/chart.js/dist/chart.umd.js',encoding='utf-8').read().replace('</script>','<\\/script>'))
open('goblin-birzha.html','w',encoding='utf-8').write(s)
print(len(s))

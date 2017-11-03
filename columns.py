


l = ['exiv2-devel', 'mingw-libs', 'tcltk-demos', 'fcgi', 'netcdf',
            'pdcurses-devel', 'msvcrt', 'gdal-grass', 'iconv', 'qgis-devel',
            'qgis1.1', 'php_mapscript']
cols = 2
lenl = len(l)
split = [l[i:i + int(lenl / cols)] for i in range(0, lenl, int(lenl / cols))]

for row in zip(*split):
    print("".join(str.ljust(i, 20) for i in row))

test = [1, 2, 3, 4, 5, 6]
tested = []
for x in range(2,len(test), 2):
    test.pop(x)
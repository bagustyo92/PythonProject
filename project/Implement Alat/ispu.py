import random


def random_datas():
    datas = []
    i = 0
    for p in param:
        rnd = random.randint(0, round(tbl[i][4], 0))
        datas.append(rnd)
        i += 1

    return datas


def random_datas_range(awal, akhir):
    datas = []
    i = 0
    for p in param:
        rnd = random.randint(awal, akhir)
        datas.append(rnd)
        i += 1

    return datas


def random_datas_range_params(maxRanges):
    datas = []
    i = 0
    for p in param:
        rnd = random.randint(0, maxRanges[i])
        datas.append(rnd)
        i += 1

    return datas


def random_datas_range_params_minmax(minRanges, maxRanges):
    datas = []
    i = 0
    for p in param:
        rnd = random.randint(minRanges[i], maxRanges[i])
        datas.append(rnd)
        i += 1

    return datas


def default_max_ranges():
    maxRanges = []
    i = 0
    for p in param:
        maxRanges.append(tbl[i][4])
        i += 1

    return maxRanges


def input_datas():
    datas = []
    for p in param:
        data = input("Masukkan kadar " + p + " : ")
        datas.append(data)
    return datas


param = ['PM10', 'SO2', 'CO', 'O3', 'NO2']

tbl = [[50, 150, 350, 420, 500, 600],  # pm10   0
       [80, 365, 800, 1600, 2100, 2620],  # so2    1
       [5, 10, 17, 34, 46, 57.5],  # co     2
       [120, 234, 400, 800, 1000, 1200],  # o3     3
       [0, 0, 1130, 2260, 3000, 3750]]  # no2    4

tbl_ispu = [50, 100, 200, 300, 400, 500]

kategori = ['Baik', 'Sedang', 'Tidak Sehat', 'Sangat Tidak Sehat', 'Berbahaya']
kategori_minVal = [0, 50, 100, 200, 300]


def ispu(data, tipe):
    idxa = len(tbl[tipe]) - 1
    idxb = idxa - 1

    for i in range(len(tbl[tipe])):
        if tbl[tipe][i] > data:
            idxa = i
            idxb = idxa - 1
            break

    ia = tbl_ispu[idxa]
    ib = tbl_ispu[idxb]
    xa = tbl[tipe][idxa]
    xb = tbl[tipe][idxb]

    # print ia, ib, '/', xa, xb, '=', ia-ib, '/', xa-xb, '=', float(ia-ib)/float(xa-xb)
    # print (float(ia - ib) / float(xa - xb)), '*', (data - xb), '=', (float(ia - ib) / float(xa - xb)) * (data - xb)
    isp = (float(ia - ib) / float(xa - xb)) * (data - xb) + ib

    return int(isp)


def cariMax(datas):
    i = 0
    idxMx = 0
    mx = 0
    for d in datas:
        if d > mx:
            mx = d
            idxMx = i
        i += 1

    dtMax = [idxMx, mx]
    return dtMax


def all_ispu(datas):
    i = 0
    ispus = []
    for data in datas:
        isp = ispu(data, i)
        ispus.append(isp)
        i += 1

    return ispus


def get_ispu(datas):
    mx = cariMax(datas)
    return ispu(mx[1], mx[0])


def get_kategori(ispu):
    # idxkat = len(kategori) - 1
    for i in range(len(kategori)):
        if ispu > kategori_minVal[i]:
            idxkat = i

    return kategori[idxkat]


def get_string_kategori(val):
    return kategori[val]


def get_val_kategori(kategori_in_string, start = 0):
    i = start
    for kat in kategori:
        if kategori_in_string == kat:
            return i
        i+=1

def get_kategori_value(ispu):
    for i in range(len(kategori)):
        if ispu > kategori_minVal[i]:
            idxkat = i
    return idxkat


# get kategori, output value, input data mentahan
def get_kategori_value_all(datas):
    ispux = get_ispu(datas)

    for i in range(len(kategori)):
        if ispux > kategori_minVal[i]:
            idxkat = i

    return idxkat


def get_kategori_string_all_params(datas):
    ispux = get_ispu(datas)

    for i in range(len(kategori)):
        if ispux > kategori_minVal[i]:
            idxkat = i

    return kategori[idxkat]


def main():
    datas = random_datas()  # input datas randomly
    #   datas = input_datas()   #uncomment this, for input datas manually

    print "Data pengukuran :"
    x = 0
    for d in datas:
        print param[x], ':', d
        x += 1

    dtMax = cariMax(datas)
    # ispux = ispu(dtMax[1], dtMax[0])

    ispus = all_ispu(datas)
    print "\nHasil perhitungan ISPU :"

    x = 0
    mx = 0
    idmax = 0
    for n in ispus:
        print param[x], ':', str(n), ' (' + get_kategori(n) + ') '
        if n > mx:
            mx = n
            idmax = x
        x += 1

    print "\nKesimpulan"
    # print param[dtMax[0]], '=', ispux
    print "Kategori =", get_kategori(dtMax[1])

    # print "Max ISPU =", str(mx), " ("+param[idmax]+")"
    # print "Kategori =", get_kategori(mx)


    # main()

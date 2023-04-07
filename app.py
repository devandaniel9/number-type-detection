# Bilangan prima

'''
Langkah:
1. Pilih angka bilangan bulat positif (x > 0)
2. Jika bilangan genap = x/2
3. Jika bilangan ganjil = 3x+1
4. Lakukan sampai mencapai angka 1
'''

# Title

# List import
# import numpy as np
import math
# import streamlit as st

# from PIL import Image
from PIL import Image, ImageDraw, ImageFont

# List import
import streamlit as st
import numpy as np

aaa = """
	<style>
	@import fonts/Roboto-Regular.ttf;

	html, body, [class*="css"]  {
	font-family: 'Roboto', sans-serif;
	}
	</style>
"""

streamlit_style = """
	<style>
	@import fonts;

	[class*="css"]  {
	font-family: 'roboto';
	}
	</style>
"""

def color(text, c):
    return f"<font color={c}>{text}</font>"

st.markdown(streamlit_style, unsafe_allow_html=True)
# st.write(f"The next word is {color('red','yellow')}", unsafe_allow_html=True)

def stw(text):
    return st.markdown(text, unsafe_allow_html=True)

st.markdown('''
<style>
.katex-html {
    text-align: left;
}
</style>''',
unsafe_allow_html=True
)

# Menjalankan program
# streamlit run 'Number Type Detection 4.py'

# Streamlit
# st.write("""# Number Type Detection""")
st.markdown("# <font color='#a0ff80'>Number Type Detection</font>", unsafe_allow_html=True)
st.write('Number Type Detection adalah program yang bertujuan untuk mengecek angka dan melihat hasilnya.')
st.write('')

def prima(angka):
    check = True
    for faktor in range(2, int(angka**0.5)+1):
        if angka % faktor == 0:
            check = False

    return check

def angka_hasil(angka):
    hasil = ''

    satuan = angka // 1 % 10
    puluhan = angka // 10 % 10
    ratusan = angka // 100 % 10

    satuan_list = ['','one','two','three','four','five','six','seven','eight','nine']
    satuan_2_list = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    puluhan_list = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    ratusan_list = ['','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']

    ratusan_2 = ratusan_list[ratusan]

    if puluhan != 1 or satuan == 0:
        puluhan_2 = puluhan_list[puluhan]
        satuan_2 = satuan_list[satuan]
    else:
        puluhan_2 = ''
        satuan_2 = satuan_2_list[satuan]

    if angka < 1000 or ratusan == 0: hasil = f"{hasil}{ratusan_2}"
    else: hasil = f"{hasil} {ratusan_2}"
    if angka < 100 or puluhan == 0: hasil = f"{hasil}{puluhan_2}"
    else: hasil = f"{hasil} {puluhan_2}"
    if angka < 10 or puluhan == 1 or satuan == 0: hasil = f"{hasil}{satuan_2}"
    else: hasil = f"{hasil} {satuan_2}"
    
    return hasil

def angka_hasil_2(angka):
    if angka > 0:
        hasil = ''

        trillion = angka // 10**12 % 1000
        billion = angka // 10**9 % 1000
        million = angka // 1000000 % 1000
        thousand = angka // 1000 % 1000
        satuan = angka % 1000

        if trillion > 0:
            if angka < 10**15: hasil = f"{hasil}{angka_hasil(trillion)} trillion"
            else: hasil = f"{hasil} {angka_hasil(trillion)} trillion"

        if billion > 0:
            if angka < 10**12: hasil = f"{hasil}{angka_hasil(billion)} billion"
            else: hasil = f"{hasil} {angka_hasil(billion)} billion"

        if million > 0:
            if angka < 10**9: hasil = f"{hasil}{angka_hasil(million)} million"
            else: hasil = f"{hasil} {angka_hasil(million)} million"

        if thousand > 0:
            if angka < 1000000: hasil = f"{hasil}{angka_hasil(thousand)} thousand"
            else: hasil = f"{hasil} {angka_hasil(thousand)} thousand"
        
        if angka < 1000 or satuan == 0: hasil = f"{hasil}{angka_hasil(satuan)}"
        else: hasil = f"{hasil} {angka_hasil(satuan)}"

    else:
        hasil = "zero"

    return hasil

def romawi(angka):
    satuan = angka // 1 % 10
    puluhan = angka // 10 % 10
    ratusan = angka // 100 % 10
    ribuan = angka // 1000 % 10

    satuan_list = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    puluhan_list = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','LC']
    ratusan_list = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    ribuan_list = ['','M','MM','MMM']

    ratusan_2 = ratusan_list[ratusan]

    hasil = f"{ribuan_list[ribuan]}{ratusan_list[ratusan]}{puluhan_list[puluhan]}{satuan_list[satuan]}"
    
    return hasil

st.write('## **Pilih jenis angka**')

jenis_list = [
    "Semua",
    "Bilangan prima",
    "Bilangan genap dan ganjil",
    "Pembaca bilangan",
    "Bilangan romawi",
    "Membagi bilangan",
    "Bilangan kuadrat dan kubik",
    "Bilangan palindrome"
]
jenis = st.selectbox("Pilih jenis angka", jenis_list)

if jenis == jenis_list[0]:
    angka = st.number_input("Angka", value=60, min_value=1)

    # ---

    st.write("### Bilangan prima")

    count = 1
    check = False

    angka_list = []
    angka_list.append(1)

    for faktor in range(2, int(angka**0.5)+1):
        if angka % faktor == 0:
            angka_list.append(faktor)
            check = True
            count += 1

    if check or angka == 1:
        st.write(f"{angka} bukan bilangan prima")
    else:
        st.write(f"{angka} adalah bilangan prima")

    # ---

    st.write("### Bilangan genap dan ganjil")

    if angka % 2 == 0:
        st.write(f"{angka} adalah bilangan genap")
    else:
        st.write(f"{angka} adalah bilangan ganjil")

    # ---

    st.write("### Pembaca bilangan")

    st.write(f"{angka} = {angka_hasil_2(angka)}")

    # ---

    st.write("### Bilangan romawi")

    st.write(f"{angka} = {romawi(angka)}")

if jenis == jenis_list[1]:
    st.write('**Bilangan Prima** adalah bilangan yang dapat dibagi dengan 1 dan bilangan itu sendiri.')

    jenis_2_list = ["Cek bilangan prima", "List", "Grafik"]
    jenis_2 = st.selectbox("Pilih jenis angka", jenis_2_list)

    st.write('## **Input Angka**')

    if jenis_2 == jenis_2_list[0]:
        # st.write('Masukkan angka sampai 10^12')

        angka = st.number_input("Angka", value=60, min_value=1)

        st.write('## **Hasil Penyelesaian**')

        count = 1
        check = False

        angka_list = []
        angka_list.append(1)

        for faktor in range(2, int(angka**0.5)+1):
            if angka % faktor == 0:
                angka_list.append(faktor)
                check = True
                count += 1

        angka_2_list = list(angka_list)

        for n in range(len(angka_list)):
            if angka != angka_list[len(angka_list)-n-1]**2:
                angka_2_list.append(int(round(angka / angka_list[len(angka_list)-n-1], 0)))
                count += 1

        if check or angka == 1:
            if len(angka_2_list) <= 4:
                st.write(f"**{angka}** bukan bilangan prima, karena dapat dibagi dengan {angka_2_list[1]}. Bilangan tersebut squarefree, karena punya 2 faktor prima.")
            else:
                st.write(f"**{angka}** bukan bilangan prima, karena dapat dibagi dengan {angka_2_list[1]}.")
        else:
            st.write(f"**{angka}** adalah bilangan prima")

        st.write(f"Jumlah faktor = {count}")

        aaa = ""
        faktor = 2
        count_2 = 0
        
        while faktor < 100:
            abc = prima(faktor)

            if abc:
                count = 0
                while angka % faktor == 0:
                    angka = angka / faktor
                    count += 1
                
                if count > 0:
                    if count_2 == 0:
                        aaa = f"{faktor}^{count}"
                    else:
                        aaa = f"{aaa} x {faktor}^{count}"
                    count_2 += 1

            faktor += 1

        st.write(f"Faktor prima = {aaa}")

        steps_check = st.checkbox(label="Dengan langkah", value=False)

        if steps_check:
            count = 1
            for n in angka_2_list:
                st.write(f"{count} = {n}")
                count += 1

    if jenis_2 == jenis_2_list[1]:
        angka = st.number_input("Dari angka", value=2, min_value=2)
        angka_2 = st.number_input("Ke angka", value=100, min_value=2)

        st.write('## **Hasil Penyelesaian**')

        count = 1

        for angka_3 in range(angka, angka_2):
            check = True

            for faktor in range(2, int(angka_3**0.5)+1):
                if angka_3 % faktor == 0:
                    check = False

            if check:
                st.write(f"{count} = {angka_3}")
                count += 1

            if count > 100: break

    if jenis_2 == jenis_2_list[2]:
        button_3 = st.checkbox(label="Langsung buat", value=False)

        jenis_3_list = ["Jumlah faktor", "Tidak tau"]
        jenis_3 = st.selectbox("Pilih jenis angka", jenis_3_list)

        if jenis_3 == jenis_3_list[0]:
            button_4 = st.checkbox(label="Logarithmic scale", value=False)

            limit = st.number_input("Dari angka", value=1, min_value=1)
            limit_2 = st.number_input("Ke angka", value=1000, min_value=1)

            button = st.button(label="Buat")

            if button or button_3:
                import matplotlib.pyplot as plt
                from PIL import Image

                angka_2 = []
                iteration_2 = []

                maximum = 0

                # Menyusun angka
                for angka in range(limit, limit_2):
                    angka_2.append(angka)
                    iteration = 0

                    count = 1
                    check = False

                    angka_list = []
                    angka_list.append(1)

                    for faktor in range(2, int(angka**0.5)+1):
                        if angka % faktor == 0:
                            angka_list.append(faktor)
                            check = True
                            count += 1

                    angka_2_list = list(angka_list)

                    for n in range(len(angka_list)):
                        if angka != angka_list[len(angka_list)-n-1]**2:
                            angka_2_list.append(int(round(angka / angka_list[len(angka_list)-n-1], 0)))
                            count += 1

                    iteration_2.append(count)

                    if count > maximum:
                        bagus = angka
                        maximum = count
                    
                st.write(f"Maximum = {bagus}")

                plt.scatter(angka_2, iteration_2, s=1)

                if button_4:
                    plt.xscale("log")
                
                plt.savefig("Preview.png")
                img = Image.open('Preview.png')
                st.image(img, width=500)

if jenis == jenis_list[2]:
    angka = st.number_input("Angka", value=4, min_value=0)

    st.write('## **Hasil Penyelesaian**')

    if angka % 2 == 0:
        st.write(f"{angka} adalah bilangan genap")
    else:
        st.write(f"{angka} adalah bilangan ganjil")

if jenis == jenis_list[3]:    
    angka = st.number_input("Angka", value=4, min_value=0)

    st.write('## **Hasil Penyelesaian**')

    st.write(f"{angka} = {angka_hasil_2(angka)}")

if jenis == jenis_list[4]:
    angka = st.number_input("Angka", value=4, min_value=0, max_value=3999)

    st.write('## **Hasil Penyelesaian**')

    st.write(f"{angka} = {romawi(angka)}")

def jdigit(angka):
    angka1 = list(str(angka))
    teks = ''
    count = 0
    jumlah = 0
    for a in angka1:
        if count == 0:
            teks = int(a)
        else:
            teks = f'{teks}+{int(a)}'
        jumlah += int(a)
        count += 1
    return teks, jumlah

if jenis == jenis_list[5]:
    st.write('## **Input Angka**')
    pembagi = st.number_input("Membagi angka (2-10)", value=2, min_value=2, max_value=10)
    angka = st.number_input("Angka", value=12, min_value=1)

    st.write('## **Hasil Penyelesaian**')
    st.write('')

    if pembagi == 2:
        st.write(f"Bilangan yang habis dibagi 2 jika belakangnya 0, 2, 4, 6, dan 8.")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena belakangnya {angka%10}.")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena belakangnya {angka%10}.")

    if pembagi == 3 or pembagi == 9:
        st.write(f"Bilangan yang habis dibagi {pembagi} jika jumlah digit-digitnya habis dibagi {pembagi}.")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena:")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena:")
        angka1 = list(str(angka))
        teks = ''
        count = 0
        jumlah = 0
        for a in angka1:
            if count == 0:
                teks = int(a)
            else:
                teks = f'{teks}+{int(a)}'
            jumlah += int(a)
            count += 1

        if angka % pembagi == 0:
            st.write(f'Jumlah digit = {teks} = {jumlah}, dimana habis dibagi {pembagi}')
        else:
            st.write(f'Jumlah digit = {teks} = {jumlah}, dimana tidak habis dibagi {pembagi}')

    if pembagi == 4:
        st.write(f"Bilangan yang habis dibagi 4 jika 2 digit terakhir habis dibagi 4")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena 2 digit terakhir yaitu {angka%100}, habis dibagi 4.")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena 2 digit terakhir yaitu {angka%100}, tidak habis dibagi 4.")

    if pembagi == 5:
        st.write(f"Bilangan yang habis dibagi {pembagi} jika belakangnya 0 dan 5.")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena belakangnya {angka%10}.")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena belakangnya {angka%10}.")

    if pembagi == 6:
        st.write(f"Bilangan yang habis dibagi {pembagi} jika belakangnya genap (0,2,4,6,8) dan jumlah digit-digitnya habis dibagi 3.")
        teks, jumlah = jdigit(angka)
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena belakangnya {angka%10} dan jumlah digit-digitnya {jumlah}.")
            st.write(f"Jumlah = {teks} = {jumlah} (habis dibagi 3)")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena belakangnya {angka%10} dan jumlah digit-digitnya {jumlah}.")
            st.write(f"Jumlah = {teks} = {jumlah} (tidak habis dibagi 3)")

    if pembagi == 7:
        st.write(f"Bilangan yang habis dibagi {pembagi} jika bilangan dibagi 2 yaitu bagian puluhan dan satuan, dengan selisih bagian puluhan dan 2 kalinya satuan.")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, penjelasannya ada di bawah ini:")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, penjelasannya ada di bawah ini:")
        
        angka1 = angka
        count = 1
        while angka1 >= 10:
            bpuluhan = angka1 // 10
            satuan = angka1 % 10
            if bpuluhan >= 2*satuan:
                angka1 = bpuluhan-2*satuan
                st.write(f'{count}. {bpuluhan}-2*{satuan} = {angka1}')
            else:
                angka1 = 2*satuan-bpuluhan
                st.write(f'{count}. 2*{satuan}-{bpuluhan} = {angka1}')
            count += 1

        if angka % pembagi == 0:
            st.write(f'Hasilnya {angka1}, ternyata habis dibagi 7')
        else:
            st.write(f'Hasilnya {angka1}, ternyata tidak habis dibagi 7')
    
    if pembagi == 8:
        st.write(f"Bilangan yang habis dibagi 8 jika 3 digit terakhir habis dibagi 8")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena 3 digit terakhir yaitu {angka%100}, habis dibagi 8.")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena 3 digit terakhir yaitu {angka%100}, tidak habis dibagi 8.")

    if pembagi == 10:
        st.write(f"Bilangan yang habis dibagi {pembagi} jika belakangnya 0.")
        if angka % pembagi == 0:
            st.write(f"Angka **{angka}** habis dibagi {pembagi}, karena belakangnya {angka%10}.")
        else:
            st.write(f"Angka **{angka}** tidak habis dibagi {pembagi}, karena belakangnya {angka%10}.")
            
    # st.write('## **Langkah Penyelesaian**')

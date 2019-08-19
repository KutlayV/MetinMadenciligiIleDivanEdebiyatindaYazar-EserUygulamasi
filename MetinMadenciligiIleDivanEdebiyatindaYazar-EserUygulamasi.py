# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:57:19 2019

@author: hamdikutlayvelioglu
"""
import os
from math import sqrt
import xlrd
import pickle
import numpy as np

def tekrarlariTemizle(liste):
    n = len(liste)
    i = 0
    while i <= n:
        j = i+1
        while j < n:
            if liste[i] == liste[j]:
                liste.pop(j)
                j -= 1
            j += 1
            n = len(liste)
        i += 1
        n = len(liste)
    return liste

def metniTemizle(liste):
    n = len(liste)
    for i in range(0, n):
        liste[i] = liste[i].lower()
        if (liste[i] == "."):
            liste[i] = ""
        elif (liste[i] == "ve"):
            liste[i] = ""
        elif (liste[i] == "ancak"):
            liste[i] = ""
        elif (liste[i] == "ama"):
            liste[i] = ""
        elif (liste[i] == "fakat"):
            liste[i] = ""
        elif (liste[i] == "'"):
            liste[i] = ""
        elif (liste[i] == "/"):
            liste[i] = ""
        elif (liste[i] == "-"):
            liste[i] = ""

    metin = "".join(liste)
    return metin

def kelimelereAyir(metin):
    liste = list(metin)
    n = len(liste)
    n = int(n)
    kelime = ""
    a = ""
    kelimeler = []
    i = 0
    i = int(i)
    while i != n:
        if liste[i] != " ":
            while liste[i] != " ":
                kelime += liste[i]
                i += 1
            kelimeler.append(kelime)
            kelime = a
        else:
            i += 1
    return kelimeler

def boslukEkleme(liste):
    liste = list(liste)
    n = len(liste)
    if liste[n-1] != " ":
        liste.append(" ")
    return liste
def frekansVektoruBul(terimler,siirler):
    nT = len(terimler)
    nS = len(siirler)
    frekanslar = []
    for i in range(nT):
        sayac = 1
        for j in range(nS):
            if terimler[i] == siirler[j]:
                sayac += 1
        frekanslar.append(sayac)
    return frekanslar
def uzaklikHesaplama(ilkVektor,ikinciVektor):
    n = len(ilkVektor)
    #Her ikisinin eleman sayýsý da Ayný
    toplam = 0
    for i in range(n):
        toplam += (ilkVektor[i] - ikinciVektor[i])**2
    uzaklik = sqrt(toplam)
    return uzaklik
def vektorNormalizasyonu(vektor):
    n = len(vektor)
    geciciUzunluk = 0
    for i in range(n):
        geciciUzunluk += (vektor[i]) ** 2
    geciciUzunluk = sqrt(geciciUzunluk)
    for j in range(n):
        vektor[j] = vektor[j] / geciciUzunluk
    return vektor

"""
workbook = xlrd.open_workbook('divan2.xlsx')
worksheet = workbook.sheet_by_name("divan")
butunEserler = []
terimlerVektoru = []
asikCelebiSiirleri = []
adniSiirleri = []
agahSiirleri = []
ahmetPasaSiirleri = []
ahmetiDaiSiirleri = []
akifSiirleri = []
amriSiirleri = []
emriSiirleri = []
esadSiirleri = []
fatinSiirleri = []
zatiSiirleri = []
bakiSiirleri = []
fuzuliSiirleri = []
avniSiirleri = []
azizMahmudHudayiSiirleri = []
esadiBagdadiSiirleri = []
bosnaliSabitSiirleri = []
bursaliTalipSiirleri = []
cemSultanSiirleri = []
dukakinzadeAhmetSiirleri = []
fedayiSiirleri = []
nedimSiirleri = []
seyhGalipSiirleri = []
enSiirleri = []
alSiirleri = []

with open('terimlerVektoru.pickle','rb') as dosya4:
    terimlerVektoru = pickle.load(dosya4)


for i in range(1,7149):
    for j in range(0,2):
        butunEserler.append(worksheet.cell(i, j).value)
for i in range(1,7149):
    for j in range(0,2):
        butunEserler.append(worksheet.cell(i, j).value)

eserlerListesi = []
for k in range(0,7148):
    gecici = list(butunEserler[k])
    gecici = metniTemizle(gecici)
    gecici = boslukEkleme(gecici)
    gecici = kelimelereAyir(gecici)
    eserlerListesi.append(gecici)

ne = len(butunEserler)
for l in range(0,ne,2):
    if butunEserler[l] == "ADNÝ" and len(adniSiirleri) <= 20:
        adniSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AGAH" and len(agahSiirleri) <= 20:
        agahSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AHMET PAÞA" and len(ahmetPasaSiirleri) <= 20:
        ahmetPasaSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AHMET-Ý DAÝ" and len(ahmetiDaiSiirleri) <= 20:
        ahmetiDaiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AKÝF" and len(akifSiirleri) <= 20:
        akifSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AMRÝ" and len(amriSiirleri) <= 20:
        amriSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AÞIK ÇELEBÝ" and len(asikCelebiSiirleri) <= 20:
        asikCelebiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AVNÝ" and len(avniSiirleri) <= 20:
        avniSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AZÝZ MAHMUD HÜDAYÝ" and len(azizMahmudHudayiSiirleri) <= 20:
        azizMahmudHudayiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "ESADI BAÐDADÝ" and len(esadiBagdadiSiirleri) <= 20:
        esadiBagdadiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "BOSNALI SABÝT" and len(bosnaliSabitSiirleri) <= 20:
        bosnaliSabitSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "BURSALI TALÝP" and len(bursaliTalipSiirleri) <= 20:
        bursaliTalipSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "CEM SULTAN" and len(cemSultanSiirleri) <= 20:
        cemSultanSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "DUKAKÝN-ZADE AHMET" and len(dukakinzadeAhmetSiirleri) <= 20:
        dukakinzadeAhmetSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "EMRÝ" and len(emriSiirleri) <= 20:
        emriSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "ESAD"  and len(esadSiirleri) <= 20:
        esadSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "FATÝN" and len(fatinSiirleri) <= 20:
        fatinSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "FEDAYÝ" and len(fedayiSiirleri) <= 20:
        fedayiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "NEDÝM" and len(nedimSiirleri) <= 20:
        nedimSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "ÞEYH GALÝP" and len(seyhGalipSiirleri) <= 20:
        seyhGalipSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "FUZULÝ" and len(fuzuliSiirleri) <= 20:
        fuzuliSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "BAKÝ" and len(bakiSiirleri) <= 20:
        bakiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "ZATÝ" and len(zatiSiirleri) <= 20:
        zatiSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "EN" and len(enSiirleri) <= 20:
        enSiirleri += butunEserler[l+1]
    elif butunEserler[l] == "AL" and len(alSiirleri) <= 20:
        alSiirleri += butunEserler[l+1]

sairler = [adniSiirleri,agahSiirleri,ahmetPasaSiirleri,ahmetiDaiSiirleri,akifSiirleri,
           asikCelebiSiirleri,avniSiirleri,azizMahmudHudayiSiirleri,esadiBagdadiSiirleri,
           bosnaliSabitSiirleri,bursaliTalipSiirleri,cemSultanSiirleri,dukakinzadeAhmetSiirleri,
           emriSiirleri,esadSiirleri,fatinSiirleri,fedayiSiirleri,nedimSiirleri,seyhGalipSiirleri,
           fuzuliSiirleri,bakiSiirleri,zatiSiirleri,enSiirleri,alSiirleri]
for p in range(0,24):
    sairler[p] = list(sairler[p])
    sairler[p] = metniTemizle(sairler[p])
    sairler[p] = boslukEkleme(sairler[p])
    sairler[p] = kelimelereAyir(sairler[p])
frekansMatrisiSairler = []
geciciFrekansVektoru = []
nS = len(sairler)
for y in range(nS):
    geciciFrekansVektoru = frekansVektoruBul(terimlerVektoru,sairler[y])
    frekansMatrisiSairler.append(geciciFrekansVektoru)
nVektorSairlerF = len(frekansMatrisiSairler)
nE = len(eserlerListesi)
frekansMatrisiEserler = []
for y in range(nE):
    geciciFrekansVektoru = frekansVektoruBul(terimlerVektoru,eserlerListesi[y])
    frekansMatrisiEserler.append(geciciFrekansVektoru)
nEserlerF = len(frekansMatrisiEserler)
uzakliklarMatrisi = []
geciciVektor = []
for i in range(nVektorSairlerF):
    geciciVektor = []
    for j in range(len(terimlerVektoru)):
        geciciVektor.append(frekansMatrisiSairler[i][j])
        
    geciciVektor = vektorNormalizasyonu(geciciVektor)
    for k in range(len(terimlerVektoru)):
        frekansMatrisiSairler[i][k] = geciciVektor[k]
for i in range(nEserlerF):
    geciciVektor = []
    geciciVektor = frekansMatrisiEserler[i]
    geciciVektor = vektorNormalizasyonu(geciciVektor)
    for k in range(len(terimlerVektoru)):
        frekansMatrisiEserler[i][k] = geciciVektor[k]

with open('normallesmisSairlerFrekansMatrisi.pickle','wb') as dosya:
	pickle.dump(frekansMatrisiSairler,dosya)
with open('normallesmisEserlerFrekansMatrisi.pickle','wb') as dosya2:
	pickle.dump(frekansMatrisiEserler,dosya2)
    
uzakliklarMatrisi = []

for i in range(len(frekansMatrisiEserler)):
    geciciUzaklikVektoru = []
    for j in range(len(frekansMatrisiSairler)):
        geciciUzaklik = uzaklikHesaplama(frekansMatrisiEserler[i],frekansMatrisiSairler[j])
        geciciUzaklikVektoru.append(geciciUzaklik)
    uzakliklarMatrisi.append(geciciUzaklikVektoru)

sairler = ["Adni'nin Siirleri","Agah'ýn Siirleri","Ahmet Pasa'nin Siirleri","AhmetiDai'nin Siirleri","Akif'in Siirleri",
           "Asik Celebi'nin Siirleri","Avni'nin Siirleri","Aziz Mahmud Hudayi'nin Siirleri","Esadi Bagdadi'nin Siirleri",
           "Bosnali Sabit'in Siirleri","Bursali Talip'in Siirleri","Cem Sultan'ýn Siirleri","Dukakin Zade Ahmet'in Siirleri",
           "Emri'nin Siirleri","Esad'in Siirleri","Fatin'in Siirleri","Fedayi'nin Siirleri","Nedim'in Siirleri","Seyh Galip'in Siirleri",
           "Fuzuli'nin Siirleri","Baki'nin Siirleri","Zati'nin Siirleri","En Siirleri","Al Siirler"]

enKucukler = []
for i in range(len(uzakliklarMatrisi)):
    enKucukler.append(uzakliklarMatrisi[i].index(min(uzakliklarMatrisi[i])))

with open('uzakliklarMatrisi.pickle','wb') as dosya3:
	pickle.dump(uzakliklarMatrisi,dosya3)"""
with open('uzakliklarMatrisi.pickle','rb') as dosya:
    uzakliklarMatrisi = pickle.load(dosya)
enKucukler = []
for i in range(len(uzakliklarMatrisi)):
    enKucukler.append(uzakliklarMatrisi[i].index(min(uzakliklarMatrisi[i])))
enKucukler = []
for i in range(len(uzakliklarMatrisi)):
    enKucukler.append(uzakliklarMatrisi[i].index(min(uzakliklarMatrisi[i])))
    
asikCelebiSiirleri = []
adniSiirleri = []
agahSiirleri = []
ahmetPasaSiirleri = []
ahmetiDaiSiirleri = []
akifSiirleri = []
amriSiirleri = []
emriSiirleri = []
esadSiirleri = []
fatinSiirleri = []
zatiSiirleri = []
bakiSiirleri = []
fuzuliSiirleri = []
avniSiirleri = []
azizMahmudHudayiSiirleri = []
esadiBagdadiSiirleri = []
bosnaliSabitSiirleri = []
bursaliTalipSiirleri = []
cemSultanSiirleri = []
dukakinzadeAhmetSiirleri = []
fedayiSiirleri = []
nedimSiirleri = []
seyhGalipSiirleri = []
enSiirleri = []
alSiirleri = []

for i in range(len(enKucukler)):
    if enKucukler[i] == 0:
        adniSiirleri.append(i+1)
    elif enKucukler[i] == 1:
        agahSiirleri.append(i+1)
    elif enKucukler[i] == 2:
        ahmetPasaSiirleri.append(i+1)
    elif enKucukler[i] == 3:
        ahmetiDaiSiirleri.append(i+1)
    elif enKucukler[i] == 4:
        akifSiirleri.append(i+1)
    elif enKucukler[i] == 5:
        amriSiirleri.append(i+1)
    elif enKucukler[i] == 6:
        emriSiirleri.append(i+1)
    elif enKucukler[i] == 7:
        esadSiirleri.append(i+1)
    elif enKucukler[i] == 8:
        fatinSiirleri.append(i+1)
    elif enKucukler[i] == 9:
        zatiSiirleri.append(i+1)
    elif enKucukler[i] == 10:
        bakiSiirleri.append(i+1)
    elif enKucukler[i] == 11:
        fuzuliSiirleri.append(i+1)
    elif enKucukler[i] == 12:
        avniSiirleri.append(i+1)
    elif enKucukler[i] == 13:
        azizMahmudHudayiSiirleri.append(i+1)
    elif enKucukler[i] == 14:
        esadiBagdadiSiirleri.append(i+1)
    elif enKucukler[i] == 15:
        bosnaliSabitSiirleri.append(i+1)
    elif enKucukler[i] == 16:
        bursaliTalipSiirleri.append(i+1)
    elif enKucukler[i] == 17:
        cemSultanSiirleri.append(i+1)
    elif enKucukler[i] == 18:
        dukakinzadeAhmetSiirleri.append(i+1)
    elif enKucukler[i] == 19:
        fedayiSiirleri.append(i+1)
    elif enKucukler[i] == 20:
        nedimSiirleri.append(i+1)
    elif enKucukler[i] == 21:
        seyhGalipSiirleri.append(i+1)
    elif enKucukler[i] == 22:
        enSiirleri.append(i+1)
    elif enKucukler[i] == 23:
        alSiirleri.append(i+1)
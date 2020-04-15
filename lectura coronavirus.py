#leer csv.py
import csv
import numpy as np
import matplotlib.pyplot as plt


def main():


	Fecha_de_diagnostico=[]
	Fecha_muertos=[]
	Numero_de_muertos=[]
	Tipo=[]
	Pais_de_origen=[]
	Contagios_por_fecha={}
	Contagios_por_fecha_muertos={}
	Numero_de_contagios_por_fecha={}
	Numero_de_muertos_por_fecha={}
	Numero_contagios_por_pais={}
	Contagios_por_tipo={}
	Contagios_por_pais={}
	Numero_de_casos_muertos=0
	Numero_de_casos_recuperados=0
	Numero_de_casos_muertos_en_bogota=0
	Numero_de_casos_recuperados_en_bogota=0

	with open('Casos1 (4).csv' ,encoding='utf-8') as File:
		reader= csv.DictReader(File)

		for row in reader:			
			Fecha_de_diagnostico.append(row['Fecha de diagnóstico'])
			Fecha_muertos.append(row['Atención**'])
			Tipo.append(row['Tipo*'])			
			Pais_de_origen.append(row['País de procedencia'])

			if( row['Atención**']=='Fallecido'):								
				Numero_de_casos_muertos += 1
				if(row['Departamento o Distrito']=='Bogotá D.C.'):
					Numero_de_casos_muertos_en_bogota +=1
			elif(row['Atención**']=='Recuperado' or row['Atención**']=='Recuperado (Hospital)'):
				Numero_de_casos_recuperados += 1
				if(row['Departamento o Distrito']=='Bogotá D.C.'):
					Numero_de_casos_recuperados_en_bogota +=1
			#print(row)


	Contagios_por_fecha=Contagiados_diarios(Fecha_de_diagnostico)	
	Numero_de_contagios_por_fecha=Numero_Contagiados_diarios(Contagios_por_fecha)

	Contagios_por_fecha_muertos=Contagiados_diarios(Fecha_muertos)	
	Numero_de_muertos_por_fecha=Numero_Contagiados_diarios_datos(Contagios_por_fecha_muertos)

	Contagios_por_tipo=Contagiados_diarios(Tipo)	
	Numero_contagios_por_tipo=Numero_Contagiados_diarios_datos(Contagios_por_tipo)


	porcentaje_muertos_bogota=(int(Numero_de_casos_muertos_en_bogota)*100)/(int(Numero_de_casos_muertos))
	porcentaje_recuperados_bogota=(int(Numero_de_casos_recuperados_en_bogota)*100)/(int(Numero_de_casos_recuperados))


	print('Numero de casos muertos {}'.format(Numero_de_casos_muertos))
	print('Numero de casos Recuperado {}'.format(Numero_de_casos_recuperados))
	print('\n')
	print('Numero de casos muertos en Bogotá {}'.format(Numero_de_casos_muertos_en_bogota))
	print('Numero de casos recuperados en Bogotá {}'.format(Numero_de_casos_recuperados_en_bogota))
	print('\n')
	print('porcentaje de muertos en Bogotá {0:.3f} %'.format(porcentaje_muertos_bogota))
	print('porcentaje de recuperados en Bogotá {0:.3f} %'.format(porcentaje_recuperados_bogota))
	
	graficar(Numero_de_contagios_por_fecha,Numero_de_muertos_por_fecha,Numero_contagios_por_tipo)	



	
	


def graficar(Numero_de_contagios_por_fecha,Numero_de_muertos_por_fecha,Numero_contagios_por_tipo):

	keys2 = Numero_contagios_por_tipo.keys()
	values2 =Numero_contagios_por_tipo.values()

	keys1 = Numero_de_muertos_por_fecha.keys()
	values1 =Numero_de_muertos_por_fecha.values()

	keys = Numero_de_contagios_por_fecha.keys()
	values = Numero_de_contagios_por_fecha.values()
	
	Fig=plt.subplots(1, figsize=(20,20)) 

	plt.subplot(2,2,1)
	colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85","#60D394"]
	explode=[0.1, 0.1, 0.3, 0.2, 0.1, 0.1]
	plt.pie(list(values1), labels=list(keys1),autopct="%0.1f %%",explode=explode,shadow=True,pctdistance=0.6,radius=0.9)
	plt.title("Clasificacion de casos")	
	plt.axis("equal")
	
	plt.subplot(2,2,2)
	explode=[0.03, 0.03, 0.03]
	plt.pie(list(values2), labels=list(keys2),autopct="%0.1f %%", explode=explode,shadow=True,radius=0.9)
	plt.title("Tipo de contagio")	
	plt.axis("equal")
	

	plt.subplot(2,1,2)
	plt.bar(list(keys), list(values))
	plt.grid(True)
	plt.title("Casos de coronavirus En colombia")	
	
	
	plt.xticks( rotation=45, ha='right')
	plt.xlabel('Fecha de diagnóstico')
	plt.ylim(0, 3000)  
	plt.ylabel('Numero de casos')
	plt.legend('Acumulado de casos coronavirus',loc='upper center')
	#plt.xticks(mapeado, meses) 
	plt.show()
	#plt.savefig("Coronavirus colombia.pdf")


def Contagiados_diarios(Fecha_de_diagnostico):

	Fecha_de_diagnostico_vista ={}
	for idx, letter in enumerate(Fecha_de_diagnostico): # se obtiene el indice y la letra
		if letter not in Fecha_de_diagnostico_vista:			# si la letra no esta dentro de las letras que no hemos visto
			Fecha_de_diagnostico_vista[letter]=(idx,1) 		# (indice, cuantas veces se ha visto esa letra)			
			# se carga en el diccionario la letra encontrada y la cantidad de veces que se encontro
		else:
			Fecha_de_diagnostico_vista[letter]=(Fecha_de_diagnostico_vista[letter][0]+1,Fecha_de_diagnostico_vista[letter][1]+1)  
			#print(Fecha_de_diagnostico_vista)			
	return Fecha_de_diagnostico_vista


def Numero_Contagiados_diarios(Fecha_de_diagnostico_vista):
	Numero_de_casos_diarios={}

	for key,value in Fecha_de_diagnostico_vista.items():
		#print(Fecha_de_diagnostico_vista[key])
		if value[1]!=0:
			Numero_de_casos_diarios[key]=(value[0]+1)	
			#print(Numero_de_casos_diarios[key])		
		elif value[1]==1:
			Numero_de_casos_diarios[key]=(value[1])
			#print(Numero_de_casos_diarios[key])

	return Numero_de_casos_diarios
	
def Numero_Contagiados_diarios_datos(Fecha_de_diagnostico_vista):
	Numero_de_casos_diarios={}

	for key,value in Fecha_de_diagnostico_vista.items():
		#print(Fecha_de_diagnostico_vista[key])
		if value[1]!=0:
			Numero_de_casos_diarios[key]=(value[1])	
			#print(Numero_de_casos_diarios[key])		


	return Numero_de_casos_diarios

if __name__ == '__main__':
	main()
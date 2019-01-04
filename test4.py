# -*- coding: utf-8 -*-
from openpyxl import Workbook       # 라이브러리 설치 pip install openpyxl
from openpyxl import load_workbook  # 엑셀읽어오기 위한 라이브러리
import os

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
통합
나눈 텍스트 파일들 text0으로 통합 
**주의 text0이 이미 존재하면 실행 안됨 따라서 text0 지워주고 실행 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#폴더별 파일개수 자동으로 가져오기
def count_files():
    amount=[]  #for문 밖에 변수 설정해줘야 초기화 안된다!!
    for quarter_n in range(1,5):
        list = os.listdir("C:/Users/User/Desktop/pythonproject/result/quarter{0}/".format(quarter_n))
        number_files = len(list)
        
        amount.append(("quarter{0}".format(quarter_n),number_files))  #(폴더명,폴더안파일개수)
        #amount = [('quarter1', 176), ('quarter2', 144),('quarter3', 120),('quarter4', 121)] 
        
    print(amount)
    return amount


def main():
    Result_Path="C:/Users/User/Desktop/pythonproject/result/"
    folder_file_count=[]
    folder_file_count=count_files()
    
    print(folder_file_count)
   
    for (fname,fcount) in folder_file_count:
        fw=open(Result_Path+"{0}/text0.txt".format(fname),'a', encoding='UTF8')  #파일 쓰기 위함
        
        tot = fcount+1
        for i in range(1,tot):
            fr=open(Result_Path+"{0}/text{1}.txt".format(fname,i),'r', encoding='UTF8') #파일 읽어오기 위함
            line= fr.readlines() #list로 받아옴

            fw.writelines(line) #list안에 있는 문자열을 연속해서 출력(list에 \n 있는 경우 )   
            fw.write("\n")
          
            
        fr.close()
        fw.close()

main()

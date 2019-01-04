# -*- coding: utf-8 -*-
from openpyxl import Workbook       # 라이브러리 설치 pip install openpyxl
from openpyxl import load_workbook  # 엑셀읽어오기 위한 라이브러리



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
openpyxl 라이브러리를 이용하여 엑셀 파일을 읽어서 
4분기 별로 나눠서 초록의 각 셀의 내용들을 각 text file에 저장 
*파일이름 1부터 시작하
1분기(2004~6)  txt 1~175
2분기(2007~9)  txt 1~
3분기(2010~12) txt 1~
4분기(2013~15) txt 1~
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def create_txt(mode,txt_num,row_contents):    
    if mode=="q1":
        f=open("result/quarter1/text{0}.txt".format(txt_num),'w', encoding='UTF8')
        f.write(row_contents)
    elif mode=="q2":
        f=open("result/quarter2/text{0}.txt".format(txt_num),'w', encoding='UTF8')
        f.write(row_contents)
    elif mode=="q3":
        f=open("result/quarter3/text{0}.txt".format(txt_num),'w', encoding='UTF8')
        f.write(row_contents)
    else:
        f=open("result/quarter4/text{0}.txt".format(txt_num),'w', encoding='UTF8')
        f.write(row_contents)
    f.close()
    
    
def main(): 
    #Data파일 가져오기
    wb = load_workbook('data_560.xlsx') 
    sheet1 = wb.active #읽을 Data파일 스프레드 시트 설정
    
    sheet1.delete_rows(1)  #첫 행 헤더 부분 지우기
     
    txt_num1=0
    txt_num2=0
    txt_num3=0
    txt_num4=0
    #읽어오기
    for r in sheet1.rows:
        row_contents = r[1].value #초록    r[1].value 두번쨰 칼럼의 셀 내용 저장
        row_yyyymm=str(r[2].value) #발행연도 int값으로 받아옴 !!  슬라이싱을 위해 str 변환 
        
        year=int(row_yyyymm[0:4])  #연도만 추출 str형
        
        if year<2007:
            txt_num1+=1
            create_txt("q1",txt_num1,row_contents)
        elif 2007<=year<2010:
            txt_num2+=1
            create_txt("q2",txt_num2,row_contents)
        elif 2010<=year<2013:
            txt_num3+=1
            create_txt("q3",txt_num3,row_contents)
        else:
            txt_num4+=1
            create_txt("q4",txt_num4,row_contents)
            
    wb.close()

main()
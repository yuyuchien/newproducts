# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 20:19:05 2021

@author: user
"""
import random

print('----歡迎光臨猜數挑戰----')
print('規則說明:    有10次猜題機會')
print('            超過10次須重新挑戰')
print('            猜數範圍自行設定')
print('            答對沒有獎品')
print('-'*40)
print('挑戰開始!')

minv=int(input('請輸入範圍最小值(負數也可):'))
maxv=int(input('請輸入範圍最大值:'))
ans=random.randint(minv,maxv)
goout=0
guess=0

while ans != guess:
    
    guess = int(input('請輸入猜數{}~{}:'.format(minv,maxv)))
    goout += 1
    
    if guess > ans:
        maxv = guess
        print('猜小一點')
    
    if guess < ans:
        minv = guess
        print('猜大一點')
        
    if goout == 8:
        print('\n剩2次機會!')
        continue
    
    if goout == 10:   
        print('\n答錯10次囉!失敗!')  
        break
    
    elif guess == ans:
        print('恭喜答對')
        break
    
    
print('-'*40)
print('遊戲結束囉!再挑戰一次吧!')
        
            
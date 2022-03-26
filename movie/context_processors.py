import requests



# def requestNews(count):
#     return 
    

# while True:
#     if(count_page == 1):
#         result_api_new = requests.get(f'https://newsdata.io/api/1/news?apikey=pub_5737d339b2e69bf48a18b40f51fe63b33747&language=en&category=entertainment&page={count_page}').json()
#         print('Seyfe Deyerim ', count_page)
#         for i in result_api_new['results']:
#             #print(i['image_url'])
#             if(i['image_url'] != None):
#                 news_image.append(i)
#         #print('sekil listesi ', len(news_image))
#                 if(len(news_image) == 4):
#                     print('Uzunlug 4 Dur Stop')
#                 elif(len(result_api_new['results']) == 10):
#                     print('fuck')
#                     count_page += 1
#                     print(len(news_image))
#                     print('imege list helede 4 den kicikdir ', len(news_image))
#     else:
#         #!Son 4 xeberi alma amma sekile diqqet et cunki none gelenler var
#         print('Noldu Amk Seyfe Necedeyem ', count_page)
#         print('Seyfe 2 den baslayanda listin uzunlugu ', len(news_image))
#         #*break bunu istifade edersen burda
#         result_api_new = requests.get(f'https://newsdata.io/api/1/news?apikey=pub_5737d339b2e69bf48a18b40f51fe63b33747&language=en&category=entertainment&page={count_page}').json()
        
#         for i in result_api_new['results']:
#             if(i['image_url'] != None):
#                     news_image.append(i)
        
#         if(len(news_image) == 4):
#             print('4 Lu data geldi')
#             break
        
#         print('Isledi Deyesen 1 den basqa deyerlerde page deyeri olaraq')
#         for i in result_api_new['results']:
#             #print('Resutl Api View Value ', result_api_new['results'][i])#0 indi index title deyerini donderir
#             #print(i['title'])
#             print('-------------------------------------------------------------------------------------------------')
#             if(i == len(result_api_new['results'])):
#                 count_page += 1
#                 print('Count Page In Deyeri Deyisdi Kecdi Diger Seyfeye ', count_page)
#             else:
#                 if(i['image_url'] != None):
#                     news_image.append(i)
#                 else:
#                     print('Xeberin Sekili', i['image_url'])
#                 #print('Title ', i['title'])

#     #print(len(result_api_new['results']))
#         # print('Image Url ', i['image_url'])
#         # print('--------------------------------')


#     #!En Son Xeberi Veren Hisse
#     #print('En Son Xeber ', result_api_new['results'][-1])


# result_api_new = None
# news_image = []
# count_page = 1
# while True:
#     result_api_new = requests.get(f'https://newsdata.io/api/1/news?apikey=pub_5737d339b2e69bf48a18b40f51fe63b33747&language=en&page={count_page}').json()
#     print('En sonuncu xeber : ', result_api_new['results'])
#     for i in result_api_new['results']:
#         if(i['image_url'] != None) and len(news_image)<4:
#             news_image.append(i)
#             print(i['image_url'])

#     if(len(news_image) == 4):#mene 4 dene lazim idi ona gy
#         print('Sekilli Gelen Datani Uzunlugu 4 BERABERIDR')
#         break
#     else:
#         count_page+=1
#         print('Isledim Aq')
#         print(result_api_new['nextPage'])


# def getNewsView(request):
#     result_api_new = None
#     news_image = []
#     count_page = 1
#     while True:
#         result_api_new = requests.get(f'https://newsdata.io/api/1/news?apikey=pub_5737d339b2e69bf48a18b40f51fe63b33747&language=en&page={count_page}').json()
#         print('En sonuncu xeber : ', result_api_new['results'][-1])
#         for i in result_api_new['results']:
#             if(i['image_url'] != None) and len(news_image)<4:
#                 news_image.append(i)
#                 print(i['image_url'])
        
#         if(len(news_image) == 4):#mene 4 dene lazim idi ona gy
#             print('Sekilli Gelen Datani Uzunlugu 4 BERABERIDR')
#             return {'news_image': news_image}
#         else:
#             count_page+=1
#             print('Isledim Aq')
#             print(result_api_new['nextPage'])


#?Test Request

# result_api_new = requests.get(f'https://newsdata.io/api/1/news?apikey=pub_5737d339b2e69bf48a18b40f51fe63b33747&language=en&page={2}').json()
# for i in result_api_new['results']:
#     print(i['image_url'])
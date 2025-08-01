import pandas as pd
import matplotlib.pyplot as plt
data113 = pd.read_csv("113年全般詐欺手法及詐騙管道.csv",encoding="utf-8",usecols=[0,2,3])
#第七行匯入csv檔案，usecols取得特定欄位
print(data113.count())#查無是否有缺失值

#10行~13行，進行詐騙管道的分類，為避免索引值因分類時被打亂，故設定reset_index(drop=True)
#reset_index重新設定索引值，(drop=True)將原本的索引值去掉

data113_internetfraud = data113.loc[(data113["詐騙管道"]=="網路詐騙")].reset_index(drop=True)
data113_gangsterPhonecall = data113.loc[(data113["詐騙管道"]=="接獲歹徒電話")].reset_index(drop=True)
data113_directContact = data113.loc[(data113["詐騙管道"]=="直接與人接觸")].reset_index(drop=True)
data113_receiveSMS = data113.loc[(data113["詐騙管道"]=="接獲手機簡訊")].reset_index(drop=True)

#取得所有詐騙手法的總數與重設索引值，新增欄位年度113
data113_internetfraudMethods_counts = data113["詐騙手法"].value_counts().reset_index()
data113_internetfraudMethods_counts.insert(0,column="年度",value=113)

#取得所有詐騙管道之網路詐騙的總數與重設索引值
data113_internetfraud_counts = data113_internetfraud["詐騙管道"].value_counts().reset_index()

#取得所有詐騙管道之總類的總數與重設索引值
data113_internetfraud_counts= data113.loc[(data113["詐騙管道"]=="網路詐騙")].value_counts().reset_index()
data113_gangsterPhonecall_counts= data113.loc[(data113["詐騙管道"]=="接獲歹徒電話")].value_counts().reset_index()
data113_directContact_counts = data113.loc[(data113["詐騙管道"]=="直接與人接觸")].value_counts().reset_index()
data113_receiveSMS_counts = data113.loc[(data113["詐騙管道"]=="接獲手機簡訊")].value_counts().reset_index()
data113_Receive_voicecall = data113.loc[(data113["詐騙管道"]=="接獲電話語音")].value_counts().reset_index()

#第30行-查看每個類別出現的次數
print(data113["詐騙管道"].value_counts())
#第32行-查看整體資訊摘要
print(data113.info())
#第34行-設定matplotlib的字型為微軟正黑體Microsoft JhengHei)，在執行圖表時，有含中文的文字不會出現亂碼或空白。
plt.rcParams["font.family"] = "Microsoft JhengHei"
#第36行-value_counts()：計算每個「詐騙管道」出現的次數
data113fraudchannel_counts = data113["詐騙管道"].value_counts().reset_index()
#第38行-將欄位名稱改為「詐騙管道」與「數量」(重新命名欄位)
data113fraudchannel_counts.columns = ["詐騙管道", "數量"]

#113年嘉義市詐騙管道總案件數
plt.figure(figsize=(10,5)) #設定畫布
#第43行-plt.bar畫直條圖
plt.bar(data113fraudchannel_counts["詐騙管道"],
        data113fraudchannel_counts["數量"],
        zorder=10,width=0.7)
#第47行-只加 y 軸的格線，並將格線放到長條圖之後，方便用於對照y軸值
plt.grid(axis="y",zorder=0)
plt.title("113年嘉義市詐騙管道案件數",fontsize=14)
#第50~51行-在每個長柱的上方標示數值，較易查看該長條圖的數量，ha="center"：水平置中對齊柱子
for i,value in enumerate(data113fraudchannel_counts["數量"]):
    plt.text(i, value, value, ha="center",va="bottom",fontsize=14)

plt.xticks(fontsize=13) # X軸字體大小設定
plt.ylim(0,2350) # y軸最大值為 2350（可依實際數值微調）
plt.ylabel("案件數",fontsize=14) # y軸標籤為「案件數」
plt.tight_layout() #自動調整間距避免重疊
plt.savefig("113年嘉義市詐騙管道案件數.png") #儲存圖檔
plt.show() #顯示圖表

#===========================================================
#以下為執行時遇到的困難，當建立圖例時，因畫布太小，圖例的邊邊會被切割掉

# data113_internetfraudcountsProfiling_top1 = pd.DataFrame(
#     {"詐騙手法":["假投資","假網拍","解除分期付款(騙賣家)","假交友(投資詐財)","中獎通知"],
#     "數量":[545,305,229,171,150],
#     "數據分離":[0.11,0,0,0,0]})
# fig, ax = plt.subplots(figsize=(8,7), 
#                        facecolor = "#272727",
#                        subplot_kw=dict(aspect="equal"))
# plt.pie(data113_internetfraudcountsProfiling_top1["數量"],
#         autopct= "%.1f%%",
#         explode = data113_internetfraudcountsProfiling_top1["數據分離"],
#         textprops={'color':'w', 'weight':'bold', 'size':13})
# plt.legend(data113_internetfraudcountsProfiling_top1["詐騙手法"],
#            bbox_to_anchor=(1, 0, 0, 1),
#            edgecolor = "#5B5B5B",
#            fontsize=15)
# plt.title("113年嘉義市網路詐騙前五名",
#           fontsize = 18,
#           color="#FFFFFF",
#           weight='bold')
# plt.savefig("113年嘉義市網路詐騙前五名之錯誤.png")
# plt.show()    
#---------------------------------------------------
#113年嘉義市網路詐騙案件數前五名-圓餅圖
#先進行了資料建構，建立圓餅圖 plt.pie
data113_internetfraudcountsProfiling_top1 = pd.DataFrame(
    {"詐騙手法":["假投資","假網拍","解除分期付款(騙賣家)","假交友(投資詐財)","中獎通知"],
    "數量":[545,305,229,171,150],
    "數據分離":[0.11,0,0,0,0]})
#建立畫布，將背景顏色改為"#272727"(深灰色)，
#subplot_kw=dict(aspect="equal")表示 x 軸與 y 軸的單位長度相等，讓圓餅圖呈現完美的圓
fig, ax = plt.subplots(figsize=(11,8), 
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal")) 
#"數據分離"利用explode凸顯「假投資」，將圓餅圖的「假投資」區塊分離出來
#textprops-設定文字屬性(顏色、字形、文字大小)
plt.pie(data113_internetfraudcountsProfiling_top1["數量"],
        autopct= "%.1f%%",
        explode = data113_internetfraudcountsProfiling_top1["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})

#plt.legend-建立圖例，設定文字內容、位置、圖例框線、文字大小
plt.legend(data113_internetfraudcountsProfiling_top1["詐騙手法"],#圖例內的文字內容
           bbox_to_anchor=(0.85, 0, 0.3, 1), #圖例的位置
           edgecolor = "#5B5B5B",#圖例框線
           fontsize=15)#文字大小

#plt.title-設定整張圖的標題(預設最上方)、文字內容、文字大小、顏色、字形
plt.title("113年嘉義市網路詐騙前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市網路詐騙前五名之假投資.png")#儲存圖檔
plt.show()  #顯示圖表



#113年嘉義市網路詐騙前五名之假網拍-圓餅圖
data113_internetfraudcountsProfiling_top2 = pd.DataFrame(
    {"詐騙手法":["假投資","假網拍","解除分期付款(騙賣家)","假交友(投資詐財)","中獎通知"],
    "數量":[545,305,229,171,150],
    "數據分離":[0,0.11,0,0,0]})
fig, ax = plt.subplots(figsize=(11,8), 
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_internetfraudcountsProfiling_top2["數量"],
        autopct= "%.1f%%",
        explode = data113_internetfraudcountsProfiling_top2["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_internetfraudcountsProfiling_top2["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市網路詐騙前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市網路詐騙前五名之假網拍.png")
plt.show()   

#113年嘉義市網路詐騙前五名之解除分期付款(騙賣家)-圓餅圖
data113_internetfraudcountsProfiling_top3 = pd.DataFrame(
    {"詐騙手法":["假投資","假網拍","解除分期付款(騙賣家)","假交友(投資詐財)","中獎通知"],
    "數量":[545,305,229,171,150],
    "數據分離":[0,0,0.11,0,0]})
fig, ax = plt.subplots(figsize=(11,8), 
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_internetfraudcountsProfiling_top3["數量"],
        autopct= "%.1f%%",
        explode = data113_internetfraudcountsProfiling_top3["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_internetfraudcountsProfiling_top3["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市網路詐騙前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市網路詐騙前五名之解除分期付款(騙賣家).png")
plt.show()

#113年嘉義市網路詐騙前五名之假交友(投資詐財)-圓餅圖
data113_internetfraudcountsProfiling_top4 = pd.DataFrame(
    {"詐騙手法":["假投資","假網拍","解除分期付款(騙賣家)","假交友(投資詐財)","中獎通知"],
    "數量":[545,305,229,171,150],
    "數據分離":[0,0,0,0.11,0]})
fig, ax = plt.subplots(figsize=(11,8), 
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_internetfraudcountsProfiling_top4["數量"],
        autopct= "%.1f%%",
        explode = data113_internetfraudcountsProfiling_top4["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_internetfraudcountsProfiling_top4["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市網路詐騙前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市網路詐騙前五名之假交友(投資詐財).png")
plt.show()  

#113年嘉義市網路詐騙前五名之中獎通知-圓餅圖
data113_internetfraudcountsProfiling_top5 = pd.DataFrame(
    {"詐騙手法":["假投資","假網拍","解除分期付款(騙賣家)","假交友(投資詐財)","中獎通知"],
    "數量":[545,305,229,171,150],
    "數據分離":[0,0,0,0,0.11]})
fig, ax = plt.subplots(figsize=(11,8), 
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_internetfraudcountsProfiling_top5["數量"],
        autopct= "%.1f%%",
        explode = data113_internetfraudcountsProfiling_top5["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_internetfraudcountsProfiling_top5["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市網路詐騙前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("中獎通知.png")
plt.show()  

#---------------------------------------------------
#113年嘉義市接獲歹徒電話案件數前五名圓餅圖
data113_gangsterPhonecallcounts_top1= pd.DataFrame(
    {"詐騙手法":["假冒機構(公務員)詐財","猜猜我是誰","騙取金融帳戶(卡片)","假借銀行貸款詐欺","解除分期付款(騙買家)"],
    "數量":[37,28,8,7,5],
    "數據分離":[0.11,0,0,0,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_gangsterPhonecallcounts_top1["數量"],
        autopct= "%.1f%%",
        explode = data113_gangsterPhonecallcounts_top1["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})

plt.legend(data113_gangsterPhonecallcounts_top1["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙之接獲歹徒電話前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙之接獲歹徒電話之假冒機構(公務員)詐財.png")
plt.show()


#113年嘉義市接獲歹徒電話案件數前五名圓餅圖
data113_gangsterPhonecallcounts_top2= pd.DataFrame(
    {"詐騙手法":["假冒機構(公務員)詐財","猜猜我是誰","騙取金融帳戶(卡片)","假借銀行貸款詐欺","解除分期付款(騙買家)"],
    "數量":[37,28,8,7,5],
    "數據分離":[0,0.11,0,0,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_gangsterPhonecallcounts_top2["數量"],
        autopct= "%.1f%%",
        explode = data113_gangsterPhonecallcounts_top2["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})

plt.legend(data113_gangsterPhonecallcounts_top2["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙之接獲歹徒電話前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙之接獲歹徒電話之猜猜我是誰.png")
plt.show()

data113_gangsterPhonecallcounts_top3= pd.DataFrame(
    {"詐騙手法":["假冒機構(公務員)詐財","猜猜我是誰","騙取金融帳戶(卡片)","假借銀行貸款詐欺","解除分期付款(騙買家)"],
    "數量":[37,28,8,7,5],
    "數據分離":[0,0,0.11,0,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_gangsterPhonecallcounts_top3["數量"],
        autopct= "%.1f%%",
        explode = data113_gangsterPhonecallcounts_top3["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})

plt.legend(data113_gangsterPhonecallcounts_top3["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙之接獲歹徒電話前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙之接獲歹徒電話之騙取金融帳戶(卡片).png")
plt.show()

data113_gangsterPhonecallcounts_top4= pd.DataFrame(
    {"詐騙手法":["假冒機構(公務員)詐財","猜猜我是誰","騙取金融帳戶(卡片)","假借銀行貸款詐欺","解除分期付款(騙買家)"],
    "數量":[37,28,8,7,5],
    "數據分離":[0,0,0,0.11,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_gangsterPhonecallcounts_top4["數量"],
        autopct= "%.1f%%",
        explode = data113_gangsterPhonecallcounts_top4["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})

plt.legend(data113_gangsterPhonecallcounts_top4["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙之接獲歹徒電話前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙之接獲歹徒電話之假借銀行貸款詐欺.png")
plt.show()

data113_gangsterPhonecallcounts_top5= pd.DataFrame(
    {"詐騙手法":["假冒機構(公務員)詐財","猜猜我是誰","騙取金融帳戶(卡片)","假借銀行貸款詐欺","解除分期付款(騙買家)"],
    "數量":[37,28,8,7,5],
    "數據分離":[0,0,0,0,0.11]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_gangsterPhonecallcounts_top5["數量"],
        autopct= "%.1f%%",
        explode = data113_gangsterPhonecallcounts_top5["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})

plt.legend(data113_gangsterPhonecallcounts_top5["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙之接獲歹徒電話前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙之接獲歹徒電話之解除分期付款(騙買家).png")
plt.show()
#---------------------------------------------------
#113年嘉義市接獲手機簡訊案件數圓餅圖
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor="#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_receiveSMS_counts["count"][0:5],
        autopct= "%.1f%%",
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_receiveSMS_counts["詐騙手法"],
           title="接獲手機簡訊",
           bbox_to_anchor=(0.9, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市接獲手機簡訊",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市接獲手機簡訊.png")
plt.show()

#---------------------------------------------------

#113年嘉義市直接與人接觸前五名圓餅圖
data113_directContactcounts_top1= pd.DataFrame(
    {"詐騙手法":["其他","假投資","假預付型消費詐財","假借銀行貸款詐欺","騙取金融帳戶(卡片)"],
    "數量":[69,28,6,4,4],
    "數據分離":[0.11,0,0,0,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727", 
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_directContactcounts_top1["數量"],
        autopct= "%.1f%%",
        explode = data113_directContactcounts_top1["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_directContactcounts_top1["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙直接與人接觸前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙直接與人接觸之其他.png")
plt.show()

data113_directContactcounts_top2= pd.DataFrame(
    {"詐騙手法":["其他","假投資","假預付型消費詐財","假借銀行貸款詐欺","騙取金融帳戶(卡片)"],
    "數量":[69,28,6,4,4],
    "數據分離":[0,0.11,0,0,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727", 
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_directContactcounts_top2["數量"],
        autopct= "%.1f%%",
        explode = data113_directContactcounts_top2["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_directContactcounts_top2["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙直接與人接觸前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙直接與人接觸之假投資.png")
plt.show()

data113_directContactcounts_top3= pd.DataFrame(
    {"詐騙手法":["其他","假投資","假預付型消費詐財","假借銀行貸款詐欺","騙取金融帳戶(卡片)"],
    "數量":[69,28,6,4,4],
    "數據分離":[0,0,0.11,0,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727", 
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_directContactcounts_top3["數量"],
        autopct= "%.1f%%",
        explode = data113_directContactcounts_top3["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_directContactcounts_top3["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙直接與人接觸前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙直接與人接觸之假預付型消費詐財.png")
plt.show()

data113_directContactcounts_top4= pd.DataFrame(
    {"詐騙手法":["其他","假投資","假預付型消費詐財","假借銀行貸款詐欺","騙取金融帳戶(卡片)"],
    "數量":[69,28,6,4,4],
    "數據分離":[0,0,0,0.11,0]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727", 
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_directContactcounts_top4["數量"],
        autopct= "%.1f%%",
        explode = data113_directContactcounts_top4["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_directContactcounts_top4["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙直接與人接觸前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙直接與人接觸之假借銀行貸款詐欺.png")
plt.show()


data113_directContactcounts_top5= pd.DataFrame(
    {"詐騙手法":["其他","假投資","假預付型消費詐財","假借銀行貸款詐欺","騙取金融帳戶(卡片)"],
    "數量":[69,28,6,4,4],
    "數據分離":[0,0,0,0,0.11]})
fig, ax = plt.subplots(figsize=(11,8),
                       facecolor = "#272727", 
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_directContactcounts_top5["數量"],
        autopct= "%.1f%%",
        explode = data113_directContactcounts_top5["數據分離"],
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_directContactcounts_top5["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市詐騙直接與人接觸前五名",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市詐騙直接與人接觸之騙取金融帳戶(卡片).png")
plt.show()
#接獲電話語音
fig, ax = plt.subplots(figsize=(11,8), 
                       facecolor = "#272727",
                       subplot_kw=dict(aspect="equal"))
plt.pie(data113_Receive_voicecall["count"],
        autopct= "%.1f%%",
        textprops={'color':'w', 'weight':'bold', 'size':13})
plt.legend(data113_Receive_voicecall["詐騙手法"],
           bbox_to_anchor=(0.85, 0, 0.3, 1),
           edgecolor = "#5B5B5B",
           fontsize=15)
plt.title("113年嘉義市接獲電話語音",
          fontsize = 18,
          color="#FFFFFF",
          weight='bold')
plt.savefig("113年嘉義市接獲電話語音之猜猜我是誰.png")
plt.show()
    
#以下為統整資料區
#data113_internetfraud:113年詐騙管道==網路詐騙
#data113_gangsterPhonecall:113年詐騙管道==接獲歹徒電話
#data113_directContact:113年詐騙管道==直接與人接觸
#data113_receiveSMS:113年詐騙管道==接獲手機簡訊
#data113_internetfraud_Methods:113年的所有詐騙手法的分類與總數 
#data113_internetfraud_month:113年所有月份之網路詐騙的總數(含詐騙手法)
#data113_internetfraud_counts:113年網路詐騙的總數

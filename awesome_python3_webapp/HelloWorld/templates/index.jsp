<%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*"  import="java.sql.*"  %>
<%@ page errorPage="error.jsp" %>
<%@ page info="fly" %>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>
<html>
  <head><title>firstpage</title>
    <base href="<%=basePath%>">
    <meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">   
	<meta name="content-type" content="text/html; charset=UTF-8">
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
 <!--  	-->
	<link rel="stylesheet" type="text/css" href="jiou.css">
<!-- 
<script src="jquery.js" type="text/javascript"></script>
<script src="jquery.flyout.js" type="text/javascript"></script>
<script src="jquery.easing.js" type="text/javascript"></script>
-->

  <script language="javascript" src="yuan.js"></script> </head>
  <body >
  <%=getServletInfo() %>
  <div><img src="/page1/hua.jpg" width="100%" height="200" align="middle" class="item"></div><br>
  <form  action="indexmanage.jsp" name="form1" method="post" onSubmit="return check()">
   <table class="default"  width="50%" align="right">
   <tr class="title">  
    <th colspan="2"class="item">用户登录</th> </tr>
   <tr class="item">   
   <th  class="item"> 用户名：</th>
   <td > <input type="text" name="name" placeholder="用户名" ></td> </tr>
      <tr class="item">
       <th  class="item"> 密      码：   </th>  
       <td ><input type="password" name="pwd" placeholder="密码"> </td></tr>
       <tr class=item>
       <td style="color:red; border:1"colspan="2"align="center">
       <input type="radio" id="juese"name="juese"value="学生" checked>学生
       <input type="radio" id="juese"name="juese"value="教师" >教师
       </td></tr>
   <tr class="item" >
   <th colspan="2"  class="item"> 
         <input type="submit" value="登录" name="submit">
        <button> <a href="retrieve.jsp"name="forget" >忘记密码</a></button>
       <button>  <a href="MyHtml.html">注册</a></button></th></tr>
        </table>
       </form>
<center>
    <div><img src="/page1/enemy.jpg" width="58%" height="210" align="left" class="iten" ></div>
    <div><img src="/page1/enemy.jpg" width="100" height="50" align="middle" ></div>
     <div><img src="/page1/enemy.jpg" width="100" height="50" align="left" ></div>
         <div><img src="/page1/enemy.jpg" width="100" height="50" align="middle" ></div>
 <span style="color:red"> 
 进入时间是：<%= new java.util.Date()%><br>
 当前时间是：</span><span id="dtime"style="color:red"></span><br>
   <script type="text/javascript">
function showLocale(objD)
{
 var str,colorhead,colorfoot;
 var yy = objD.getYear();
 if(yy<1900) yy = yy+1900;
 var MM = objD.getMonth()+1;
 if(MM<10) MM = '0' + MM;
 var dd = objD.getDate();
 if(dd<10) dd = '0' + dd;
 var hh = objD.getHours();
 if(hh<10) hh = '0' + hh;
 var mm = objD.getMinutes();
 if(mm<10) mm = '0' + mm;
 var ss = objD.getSeconds();
 if(ss<10) ss = '0' + ss;
 var ww = objD.getDay();
 if  ( ww==0 )  colorhead="<font color=\"#FF0000\">";
 if  ( ww > 0 && ww < 6 )  colorhead="<font color=\"#373737\">";
 if  ( ww==6 )  colorhead="<font color=\"#008000\">";
 if  (ww==0)  ww="星期日";
 if  (ww==1)  ww="星期一";
 if  (ww==2)  ww="星期二";
 if  (ww==3)  ww="星期三";
 if  (ww==4)  ww="星期四";
 if  (ww==5)  ww="星期五";
 if  (ww==6)  ww="星期六";
 colorfoot="</font>"
 str = colorhead + yy + "-" + MM + "-" + dd + " " + hh + ":" + mm + ":" + ss + "  " + ww + colorfoot;
 return(str);
}
function tick()
{
 var today;
 today = new Date();
 document.getElementById("dtime").innerHTML = showLocale(today);
 window.setTimeout("tick()", 1000);
}
tick();
</script>
<a href="https://www.baidu.com" > <span style="color:red">百度</span></a><br>
<table   width="100%">
<% 
 int i=0;
while(i<4) {
  i++;
  if(i%2==0)
  {out.println("<tr bgcolor=red >");
  }
  else
  {  
  out.println("<tr bgcolor= yellow>");
  }
   out.println("<td >******************************************************************************</td>" );
   out.println("<td >******************************************************************************</td>" );
    out.println("</tr>");
  }
  %>

  </table>
</center>
 </body>
 </html>

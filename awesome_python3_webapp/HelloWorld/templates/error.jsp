<%@ page language="java" isErrorPage="true" pageEncoding="utf-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<body>
<head><title>error page</title></head>
  <body>
  错误信息为：
  <%=exception.getMessage() %><br>
  <%=exception.toString()%>
  </body>
</html>

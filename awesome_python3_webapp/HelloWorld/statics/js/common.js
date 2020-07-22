/**
 * 
 */
function isNum(num){
	for (i=0;i<num.length;i++){
		c=num.charAt(i);
		if(c!="."&&(c>'9'||c<'0'))
			return false;
	}
	return true;
}
function check(){
	
	if(document.form1.name.value=="")
		{
		window.alert("姓名不能为空");
		document.form1.name.focus();
		return false;
		}
	if(document.form1.age.value=="")
	{
	window.alert("年龄不能为空");
	document.form1.age.focus();
	return false;
	}
	if(!isNum(document.form1.age.value))
	{
	window.alert("年龄必须为数字");
	document.form1.age.focus();
	return false;
	}
	if(document.form1.pwd.value=="")
	{
	window.alert("密码不能为空");
	document.form1.pwd.focus();
	return false;
	}
	if(form1.pass.value.length<6)
	{
	window.alert("密码不能少于6位");
	document.form1.pass.focus();
	return false;
	}
	if(document.form1.confirm.value!=document.form1.pwd.value)
	{
	window.alert("两次密码不一致");
	document.form1.confirm.focus();
	return false;
	}
	if(form1.des.value.length<10)
	{
	window.alert("自我描述不能少于10个字");
	document.form1.des.focus();
	return false;	
	}
return true;
}
function loadXMLDoc()
{
	var xmlhttp;
	xmlhttp=new XMLHttpRequest();	
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
		}
	}
	xmlhttp.open("get","retrievemanage.jsp?name="+name,true);
	xmlhttp.send();
}


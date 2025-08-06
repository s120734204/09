<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"
	import="java.io.File,java.util.List,java.util.ArrayList"%>
<%
request.setCharacterEncoding("UTF-8");
//中文解碼:UTF-8
String message = "";
//設定一個字串變數

// 送出表單-透過 <form method="post"> 送出資料
//判斷是否是 POST 請求,當使用者點擊表單中的「新增資料夾」按鈕時，才會被執行
if ("POST".equalsIgnoreCase(request.getMethod())) {
	//取得表單輸入的資料夾名稱
	String folderName = request.getParameter("folderName");
	//檢查資料夾名稱是否為空
	if (folderName != null && !folderName.trim().isEmpty()) {
		//取得伺服器上的實體路徑
		String basePath = application.getRealPath("/uploads");
		//建立一個 File 物件，代表你要建立的資料夾位置
		File newFolder = new File(basePath, folderName);
		//檢查資料夾是否已存在並嘗試建立
		if (!newFolder.exists()) {
	if (newFolder.mkdirs()) {
		message = "✅ 成功建立資料夾：" + folderName;
	} else {
		message = "❌ 建立資料夾失敗";
	}
		} else {
	message = "⚠️ 資料夾已存在：" + folderName;
		}
		//若輸入為空則給出提示
	} else {
		message = "請輸入資料夾名稱";
	}
}
List<String> existingFolders = new ArrayList<>();
String uploadPath = application.getRealPath("/uploads");
File uploadDir = new File(uploadPath);

if (uploadDir.exists() && uploadDir.isDirectory()) {
	File[] files = uploadDir.listFiles();
	if (files != null) {
		for (File file : files) {
	if (file.isDirectory()) {
		existingFolders.add(file.getName());
	}
		}
	}
}
%>
<html lang="zh-TW">
<head>
<meta charset="UTF-8" />
<title>雲端儲存區</title>
<style>
.left {
	position: fixed; /*固定在畫面上不會移動*/
	width: 180px;
	height: 100%;
	background: white;
	padding: 0px;
	top: 0;
	left: 0;
	border: 1px solid lightblue;
}

.right {
	margin-left: 180px; /* 須大於 left 寬度 */
	margin-top: 3.5%;
	padding: 5px;
	top: 1%;
	height: 95%;
}

.upder {
	position: fixed;
	margin-left: 180px;
	width: 95%;
	height: 50px;
	top: 0;
	left: 0;
	right: 0;
	z-index: 1000;
	border: 2.5px solid lightblue;
	background: white;
}

.circlebutton { /*設定按鈕樣式*/
	width: 80%;
	height: 50px;
	border-radius: 20px;
	background: white;
	color: black;
	font-size: 16px;
	border: 2px solid lightblue;
}

.inputbox {
	width: 80%;
	height: 30px;
	border-radius: 5px;
	font-size: 16px;
	padding: 0 10px;
	border: 2px solid lightblue;
	box-sizing: border-box;
}

.circlebutton:hover { /* 滑鼠移上去後變動樣式 */
	background-color: lightgray; /* 滑鼠移上去的背景色 */
	color: white; /* 字體變白 */
	border: 0px solid lightgray;
}
.large-text {
    font-size: 20px;

}

body {
	margin: 0;
	padding: 0;
}
</style>
</head>
<body>

	<div class="left">
		<div
			style="display: flex; align-items: center; justify-content: center; height: 50px; background: lightblue;; border: 2px solid lightblue;">
			<h3>
				資料儲存區<br>
			</h3>
		</div>
		<form method="post" action="File09.jsp">
			<div
				style="display: flex; align-items: center; justify-content: center; height: 60px; background: white;">
				<input type="text" id="folderPath" name="folderName" required
					class="inputbox" placeholder="輸入資料夾名稱" />
			</div>

			<div
				style="display: flex; align-items: center; justify-content: center; height: 60px; background: white;">

				<button type="submit" class="circlebutton">新增資料夾</button>
			</div>
		</form>
		<div
			style="display: flex; align-items: center; justify-content: center; height: 60px; background: white;">
			<button class="circlebutton" onclick="alert('前往上傳功能')">上傳檔案
			</button>
		</div>
	</div>
	<div class="upder"></div>
	<div class="right">
		<h2>檔案清單</h2>
		<p><%=message%></p>
		<div>
			<%
			for (String folder : existingFolders) {
			%>
			<div class=large-text style="display:flex; align-items: center;  height: 50px; border: 1px solid lightblue;"><%=folder%></div>
			<%
			}
			%>
		</div>

	</div>
</body>
</html>

<!-- http://localhost:8080/F09/File09.jsp -->
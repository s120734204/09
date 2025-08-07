<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"
	import="java.io.File,java.util.List,java.util.ArrayList,java.io.IOException"%>
<%!// 遞迴刪除資料夾及其所有內容的方法
	public boolean deleteDirectory(File folder) {
		if (!folder.exists()) {
			return false;
		}
		if (folder.isDirectory()) {
			File[] files = folder.listFiles();
			if (files != null) {
				for (File file : files) {
					if (!deleteDirectory(file)) {
						return false;
					}
				}
			}
		}
		// 當資料夾已為空時，刪除它
		return folder.delete();
	}
%>
<%
request.setCharacterEncoding("UTF-8");
//中文解碼:UTF-8
String message = ""; //回傳是否有新增到資料夾的字串
//設定一個字串變數
String folderName = request.getParameter("folderName");

// 送出表單-透過 <form method="post"> 送出資料
//判斷是否是 POST 請求,當使用者點擊表單中的「新增資料夾」按鈕時，才會被執行
if ("POST".equals(request.getMethod())) {
	//取得表單輸入的資料夾名稱
	//檢查資料夾名稱是否為空
	if (folderName != null && !folderName.trim().isEmpty()) {
		//取得伺服器上的實體路徑
		String basePath = application.getRealPath("/uploads");
		//建立一個 File 物件，代表你要建立的資料夾位置
		File newFolder = new File(basePath, folderName);
		//檢查資料夾是否已存在並建立
		if (!newFolder.exists()) {
	if (newFolder.mkdirs()) { //建立資料夾的指令 
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
String deleteFolderName = request.getParameter("deleteFolderName");
//<input name="deleteFolderName">刪除

if (deleteFolderName != null && !deleteFolderName.trim().isEmpty()) {
	String basePath = application.getRealPath("/uploads");
	File folderToDelete = new File(basePath, deleteFolderName);
	
	if (folderToDelete.exists() && folderToDelete.isDirectory()) {
		if (deleteDirectory(folderToDelete)) {
	message = "✅ 已刪除資料夾：" + deleteFolderName;
		} else {
	message = "❌ 刪除資料夾失敗";
		}
	} else {
		message = "⚠ 資料夾不存在：" + deleteFolderName;
	}
}
//新增資料夾的部分
List<String> existingFolders = new ArrayList<>();//儲存多個字串，用來存放所有找到的資料夾名稱
String uploadPath = application.getRealPath("/uploads");//回傳虛擬路徑在伺服器上的實體路徑
File uploadDir = new File(uploadPath);// 將這個路徑轉換成一個 File 物件

if (uploadDir.exists() && uploadDir.isDirectory()) {//安全檢查，確保 /uploads 路徑確實存在，isDirectory()是資料夾
	File[] files = uploadDir.listFiles();//如果檢查通過，listFiles() 方法會讀取該資料夾內的所有檔案和子資料夾，並將它們以 File 物件的陣列形式回傳
	if (files != null) {
		for (File file : files) {
	if (file.isDirectory()) {
		existingFolders.add(file.getName()); // 如果是，就把它的名稱加到清單裡
	}
		}
	}
}

//遞迴刪除資料夾及其所有內容的方法
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
	height: 50px;
	border-radius: 20px;
	font-size: 16px;
	padding: 10px;
	border: 2px solid lightblue;
	box-sizing: border-box;
}

.circlebutton:hover { /* 滑鼠移上去後變動樣式 */
	background-color: lightgray; /* 滑鼠移上去的背景色 */
	color: white; /* 字體變白 */
	border: 0px solid lightgray;
}

.divbutton {
	width: 100%;
	height: 52px;
	font-size: 20px;
	border-radius: 10px; /* 設定圓弧度 */
	
}

.divbutton:hover {
	background-color: lightblue; /* 滑鼠移上去的背景色 */
	color: white; /* 字體變白 */
	border: 0px solid lightblue;
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
		<form method="POST" action="File09.jsp">
			<div
				style="display: flex; align-items: center; justify-content: center; height: 60px; background: white;">
				<input type="text" id="folderPath" name="folderName" required
					class="inputbox" placeholder="新增資料夾名稱" />
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
		<div
			style="display: flex; align-items: center; justify-content: center; height: 60px; background: white;">
			<button class="circlebutton" onclick="alert('查看儲存空間')">儲存空間</button></div>
	</div>
	<div class="upder"></div>
	<div class="right">
		<h2>檔案清單</h2>
		<p><%=message%></p>
		<div>
			<%
			for (String folder : existingFolders) {
			%>
			<button class=divbutton
				style="display: flex; align-items: center; height: 50px; border: 1px solid lightblue;"><%=folder%></button>
			<form method="POST" action="File09.jsp"
				onsubmit="return confirm('確定要刪除資料夾 <%=folder%> 嗎？');">
				<input type="hidden" name="deleteFolderName" value="<%=folder%>"><div
				style="display: flex; align-items: center; justify-content: center; height: 5px; background: white;"></div>
				<button type="submit" class="circlebutton"
					style="width: 80px; height: 30px;justify-content: center;">刪除</button>
			</form>
			<%
			}
			%>
			<br>
		</div>
	
	</div>
</body>
</html>

<!-- http://localhost:8080/F09/File09.jsp -->

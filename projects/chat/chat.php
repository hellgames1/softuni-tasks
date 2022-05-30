<?php
$listusers = fopen("users.txt","r") or die("Unable to open file!");
$users = fread($listusers,filesize("users.txt"));
fclose($listusers);
if (strpos($users, $_SERVER['REMOTE_ADDR']) == false) { 
	if(!isset($_GET['register'])) {
		exit("false");
	} else {
		if(strlen($_GET['register'])<=30 && ctype_alnum($_GET['register'])) {
			$myfile = fopen("users.txt", "a") or die("Unable to open file!");
			fwrite($myfile,$_SERVER['REMOTE_ADDR']."@@");
			fclose($myfile);
			$myfile = fopen($_SERVER['REMOTE_ADDR'].".txt", "w") or die("Unable to open file!");
			fwrite($myfile,$_GET['register']);
			fclose($myfile);
			print("okay");
		} else {
			print("notokay");
		}
	}
} else {
	if($_SERVER["REQUEST_METHOD"] == "POST") {
		$cuser = fopen($_SERVER['REMOTE_ADDR'].".txt","r") or die("Unable to open file!");
		$str2 = fread($cuser,filesize($_SERVER['REMOTE_ADDR'].".txt"));
		fclose($listusers);
		$str1 = $_POST['msg']."@@";
		if(strlen($str1)<=160) {
			echo strlen($str1);
			echo "<br>";
			echo $str1;
			$myfile = fopen("chat.txt", "a") or die("Unable to open file!");
			fwrite($myfile,$str2.": ".$str1);
			fclose($myfile);
		}
	} else {
		exit($_SERVER['REMOTE_ADDR']);
	}
}
?>
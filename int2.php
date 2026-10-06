<?php
session_start();
if(isset($_POST['s']))
    {
        $name=$_POST['t1']
        if(strcmp($name,'Administrator')==0)
            {
               setcookie("username",'$name',time()+30*24*60*60);
            
            $msg="<b>Welcome  ".$_COOKIE['username']."!!!<br>"."You have  been registered !!!</b>";
            echo $msg; 
    }
?>
<form method='post' action=''>
<br><br>Enter the user name:<input type='text' name='t1'><br>
<input type=
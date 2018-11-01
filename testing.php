<?php
session_start();
?>
<html>
    <head></head>
    <body>
    <style>
	#buttonF input{
		position:relative;
		font-family:Times New Roman;
		font-size:20px;
		background-color:#5ACCF2;
		border-color:#0780A8;
		border-width:10px;
		border-style:solid;
		left:50%;
		transform: translateX(-50%);
		width:225px;
		height:120px;
	}
	#buttonF input:hover{
			background-color:#3DACD1;
			border-color:#07698A;
	}
	#ButtonL{
		position:relative;
		font-family:Times New Roman;
		font-size:20px;
		background-color:#5ACCF2;
		border-color:#0780A8;
		border-width:10px;
		border-style:solid;
		left:50%;
		transform: translateX(-150%);
		width:225px;
		height:120px;

	}
	#ButtonL:hover{
			background-color:#3DACD1;
			border-color:#07698A;

	}
	#ButtonR{
		width:225px;
		height:120px;
		position:relative;
		font-family:Times New Roman;
		font-size:20px;
		background-color:#5ACCF2;
		border-color:#0780A8;
		border-width:10px;
		border-style:solid;
		left:50%;
		transform: translateX(-153.6%);

	}
	#ButtonR:hover{
			background-color:#3DACD1;
			border-color:#07698A;
	}
	#ButtonS{
		width:225px;
		height:120px;
		position:relative;
		font-family:Times New Roman;
		font-size:20px;
		background-color:#5ACCF2;
		border-color:#0780A8;
		border-width:10px;
		border-style:solid;
		left:50%;
		transform: translateX(-151.7%);

	}
	#ButtonS:hover{
			background-color:#3DACD1;
			border-color:#07698A;
	}

        #ButtonB input{
                width:225px;
                height:120px;
                position:relative;
                font-family:Times New Roman;
                font-size:20px;
                background-color:#5ACCF2;
                border-color:#0780A8;
                border-width:10px;
                border-style:solid;
                left:50%;
                transform: translateX(-50%);

        }

        #ButtonB input:hover{
                        background-color:#3DACD1;
                        border-color:#07698A;
        }

</style>
        <form method="post" action="testing.php">
	  <div id="buttonF">
            <input type="submit" name="increase" value="Forward">
          </div>
            <input type="submit" name="left" value="Left" id="ButtonL">
            <input type="submit" name="stop" value="Stop" id="ButtonS">
            <input type="submit" name="right" value="Right" id="ButtonR">
	  <div id="ButtonB">
	    <input type="submit" name="decrease" value="Backwards">
	  </div>  
	 </form>
        <?php
        if(isset($_POST['increase'])){
            if(!($_SESSION['increase'])){
                $_SESSION['increase'] = 1;
            }
	    elseif($_SESSION['increase']==2){
	    }
            else{
                $count = $_SESSION['increase'] + 1;
                $_SESSION['increase'] = $count;
            }
            if($_SESSION['increase']==0){
	           $msg = shell_exec("echo 0 >/var/www/html/testing.txt");
	        }
	        elseif($_SESSION['increase']==1){
	           $msg = shell_exec("echo 1 >/var/www/html/testing.txt");
            }
	        elseif($_SESSION['increase']==2){
	           $msg = shell_exec("echo 2 >/var/www/html/testing.txt");
	        }
	        elseif($_SESSION['increase']==-1){
	           $msg = shell_exec("echo 1 >/var/www/html/testing.txt");
            }
	        elseif($_SESSION['increase']==-2){
	           $msg = shell_exec("echo 2 >/var/www/html/testing.txt");
            }
        }
        if(isset($_POST['decrease'])){
            if(!($_SESSION['increase'])){
                $_SESSION['increase'] = -1;
	        }
	        elseif($_SESSION['increase']==-2){
            }
            else{
                $count = $_SESSION['increase'] - 1;
                $_SESSION['increase'] = $count;
            }
            if($_SESSION['increase']==0){
	           $msg = shell_exec("echo 0 >/var/www/html/testing.txt");
	        }
	        elseif($_SESSION['increase']==1){
	           $msg = shell_exec("echo 1 >/var/www/html/testing.txt");
            }
	        elseif($_SESSION['increase']==2){
	           $msg = shell_exec("echo 2 >/var/www/html/testing.txt");
        	}
        	elseif($_SESSION['increase']==-1){
	            $msg = shell_exec("echo -1 >/var/www/html/testing.txt");
	        }
	        elseif($_SESSION['increase']==-2){
	            $msg = shell_exec("echo -2 >/var/www/html/testing.txt");
	        }
        }
	elseif(isset($_POST['left'])){
	    $msg = shell_exec("echo L >/var/www/html/testing.txt");
	}
	elseif(isset($_POST['right'])){
	    $msg = shell_exec("echo R >/var/www/html/testing.txt");
	}
	elseif(isset($_POST['stop'])){
	    $msg = shell_exec("echo 0 >/var/www/html/testing.txt");
	    $_SESSION['increase']=0;
	}
	$echo = $_SESSION['increase'];
	echo "<p style='text-align:center;font-style:oblique;font-size:20px;'>Current Speed: ".$echo."</p>";
        ?>
    </body>
</html>

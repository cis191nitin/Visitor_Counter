<h1> Number of Visitors to this Point: </h1>
<h3> <? print($count) ?> </h3>
<?php exec("python ~/html/cgi-bin/update_count.py", $output); ?>
<?php
$user_agent = (string) $_SERVER['HTTP_USER_AGENT'];
$os_counts = exec("python ~/html/cgi-bin/os_pull.py", $output);
$counts_arr = explode(" ", $os_counts);
if (preg_match("/Macintosh/", $user_agent) == 1) {
	print("You are: \n");
	$argv= "mac";
	$status = exec("python ~/html/cgi-bin/os_war.py $argv");
	print($status);
} elseif (preg_match("/Windows/", $user_agent) == 1){
	print("You are: \n");
	$argv="windows";
	$status = exec("python ~/html/cgi-bin/os_war.py $argv");
	print($status);
} elseif (preg_match("/Linux/", $user_agent) == 1){
	print("You are: \n");
	$argv="linux";
	$status = exec("python ~/html/cgi-bin/os_war.py $argv");
	print($status);
} else {			        
       	print("Weirdo");
}
?>

<h2> Number of Mac Fan Boys Who Have Perished Here: </h2>
<h3> <? print($counts_arr[0]) ?> </h3>

<h2> Henchmen of Bill Gates Who Never Left...Alive: </h2>
<h3> <? print($counts_arr[1]) ?> </h3>

<h2> Those Who Have Lived to See Another Day, The Linux Users: </h2>
<h3> <? print($counts_arr[2]) ?> </h3>

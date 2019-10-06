
// this funtion use set timeout before it show the package
function time(){


timeOut = setTimeout(alertFunc, 5000);
}
function alertFunc() {
 
 alarming = document.getElementById("loader_wrapper")
 window.alert("COMPLETED!")
 window.open("package")
 window.close()
}


// check for tracking number verification before authorization.
function trackinVerification(){

	var FirstName = document.getElementById("first_name")
	var SecondName = document.getElementById("second_name")
	var trackingNumber = document.getElementById("tracking_num")

	if ((FirstName.value=="clinton") && (SecondName.value=="worlu") &&(trackingNumber.value==657) ){
		window.open ("checking")
		
	}
	else{
		window.alert("Incorrect details, please try again!")
	}

}
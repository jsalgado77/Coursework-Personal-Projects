var prodRows = document.getElementById("tbodyRows");

var prodRequest = new XMLHttpRequest();

var prodData;

var prodRowData = "";

var selectedProducts = "";

var sortOrder = "D";

prodRequest.open("GET", "/productInfo.json");

prodRequest.send();

prodRequest.onload = function() {

    prodData = JSON.parse(prodRequest.responseText);

    renderTable(prodData);
}


function renderTable(data){
    for(i=0; i<data.length; i++){
        prodRowData += "<tr><td>" + data[i].prodID + "</td><td>" + "<img src=" + data[i].prodImg + " style = 'width: 200px; height =125;'>" 
        + "</td><td id='prodName"+i+"'>"+ data[i].prodName + "</td><td>" + data[i].prodDesc + "</td><td>" + "$" + data[i].prodPrice + "</td><td>" 
    + "<input type ='number' min ='0' max ='9' id ='ProdQTY" + i + "' value = '0'" + "</td></tr>";
    }
    prodRows.innerHTML = prodRowData;
}

function confirmQTY(){

    var prodArray = []

   for(i=0; i<prodData.length; i++){

    var rowNum = i.toString();

    var columnID = "ProdQTY" + rowNum;

    var prodJSON;

    var iQTY = document.getElementById(columnID).value;

    if(iQTY > 0){
        columnID = "prodName" + rowNum;

        selectedProducts += document.getElementById(columnID).innerText + ": Qty " + iQTY + "\n";

        prodArray.push({"prodName": document.getElementById(columnID).innerText, "prodQTY": iQTY});
    }
   }

   if (selectedProducts > "" && selectedProducts != null){
       reply = confirm("Are you sure you want to order the following products?: \n" + selectedProducts + "\n" 
       );

       if(reply){

           alert("Order has been placed. Thank you. Have a fantastic day!");

           prodJSON = JSON.stringify(prodArray);

           localStorage.setItem("prodJSON", prodJSON);

           selectedProducts = "";

           prodArray = NULL;

       }

       else{
        selectedProducts = "";

       }
    }
}

function resetQTY(){

    reply = confirm("Are you sure you want to cancel your selections?")

    if (reply){
        document.getElementById("productsForm").reset();
    }

}

function sortByID(){
    prodRowData = "";
    if(sortOrder == "A"){
        prodData.sort(function(a,b){
            return a.prodID - b.prodID;
        });
        sortOrder = "D";
    }
    else{
        prodData.sort(function(a,b){
            return b.prodID - a.prodID;
        });
        sortOrder = "A";
    }
    renderTable(prodData);
}

function sortByName(){
    prodRowData = "";
    if (sortOrder == "A"){
        prodData.sort(function(a,b) {
            if (a.prodName < b.prodName){
                return -1;
            }
        });
        sortOrder = "D";
    }
    else{
        prodData.sort(function(a,b){
            if (a.prodName > b.prodName){
                return -1
            }
        });
        sortOrder = "A"
    }

    renderTable(prodData);
}

function sortByPrice(){
    prodRowData = "";
    if(sortOrder == "A"){
        prodData.sort(function(a,b){
            return a.prodPrice - b.prodPrice;
        });
        sortOrder = "D";
    }
    else{
        prodData.sort(function(a,b){
            return b.prodPrice - a.prodPrice;
        });
        sortOrder = "A";
    }
    renderTable(prodData);
}

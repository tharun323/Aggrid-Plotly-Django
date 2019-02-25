
    <!-- JAVASCRIPT CODE GOES HERE -->
    var a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,m=0,f=0;
$.ajax({
    type: "GET",
    async: false,
    url: "http://127.0.0.1:8000/test/api/Adultsdata/",

    success: function(msg){
        console.log(msg);

        for (var i=0;i<msg.length; i++)
        {
        if(msg[i].sex==="Male")
        {
        m+=1;
        }
        if(msg[i].sex==="Female")
        {
        f+=1;
        }
        if(msg[i].martial_status==="Never-married")
        {
        a+=1;
        }
        if(msg[i].martial_status==="Married-civ-spouse")
        {
        b+=1;
        }
        if(msg[i].martial_status==="Divorced")
        {
        c+=1;
        }
        if(msg[i].martial_status==="Never-married")
        {
        d+=1;
        }
        if(msg[i].martial_status==="Separated")
        {
        e+=1;
        }

        if(msg[i].martial_status==="Married-AF-spouse")
        {
        f+=1;
        }
        if(msg[i].martial_status==="Married-spouse-absent")
        {
        g+=1;
        }
        if(msg[i].martial_status==="Widowed")
        {
        h+=1;
        }
        }

    },
});
console.log(a);
    var data = [{
  values: [a,b,c,d,e,f,g,h],

  labels: ['Never-married', 'Married-civ-spouse', 'Divorced','Never-married','Separated'
  ,'Married-AF-spouse','Married-spouse-absent','Widowed'],
  type: 'pie'
}];

var layout = {
  autosize: false,
  width: 650,
  height: 400,

};
Plotly.newPlot('myDiv', data, layout, {showSendToCloud:true});

var layout2 = {
  autosize: false,
  width: 350,
  height: 400,

};
var data = [
  {
    x: ['Males', 'Females'],
    y: [m, f],
    type: 'bar'
  }
];

Plotly.newPlot('myDiv2', data,layout2);


const xValues = ["Tries1", "Tries2", "Tries3"];
const yValues = [50, 40, 30, 20, 10];
const barColors = ["#1a1a1a", "#2a2a2a","blue","orange","brown"];


//   bar chart 


var chartCanvas = document.getElementById('myChart').getContext('2d');
new Chart(chartCanvas, {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues,
      tension:0.1
    }]
  },
  options: {
    legend: {display: true},
    responsive:true,
    maintainAspectRatio:false,
    title: {
      display: FontFaceSetLoadEvent,
      text: "Game Progresss - Bar Chart"
    },
    scales:{
        y:{
            beginAtZero:true}
    }
  }
});




// // line 

const lineChartCanvas = document.getElementById('lineChart').getContext('2d');
new Chart(lineChartCanvas, {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
    //   label: "",
      borderColor: "red",
      data: yValues,
      fill: false,
      tension: 0.1
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: true },
      title: {
        display: true,
        text: "Game Progress - Line Chart"
      }
    },
    scales: {
      y: { beginAtZero: true }
    }
  }
});





  
import{
    Chart as ChartJS,
    CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend

} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);
import {Bar} from "react-chartjs-2"

function CropChart({res}){
    const data={
        labels:res.map((item)=>item.crop),
        datasets:[
            {
                label:"Confidence",
                data:res.map((item)=>item.probability),

                backgroundColor: "rgba(69, 212, 100, 0.8)",
        borderColor: "rgb(70, 229, 105)",
        borderWidth: 1,

        borderRadius: 8,
        barThickness: 18
            }
        ] 
    }
    const options = {
    indexAxis: "y",

    responsive: true,

    plugins: {
      legend: {
        labels: {
          font: {
            size: 14
          }
        }
      },

      tooltip: {
        callbacks: {
          label: function (context) {
            return ` Confidence: ${context.raw.toFixed(2)}%`;
          }
        }
      }
    },

    scales: {
      x: {
        beginAtZero: true,
        max: 100,

        ticks: {
          callback: function (value) {
            return value + "%";
          }
        },

        grid: {
          display: false
        }
      },

      y: {
        grid: {
          display: false
        }
      }
    }
  };



    return <Bar  data={data}/>
}
export {CropChart}


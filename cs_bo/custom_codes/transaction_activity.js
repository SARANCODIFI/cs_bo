frappe.ui.form.on('Customer', {
    refresh: function render_heatmap(frm) {
        let heatmap = new frappe.Chart('#myCanvas', {
			type: "heatmap",
			colors: ['#ebedf0', '#c0ddf9', '#73b3f3', '#3886e1', '#17459e'],
			domain: [0, 5, 10, 15, 25],
			countLabel: "Tradebook",
			data: {},
		});
        frappe
			.xcall("helpdesk.helpdesk.custom.transaction_activity.get_trade_book_heatmap_data", {
				ucc: cur_frm.doc.fsl_ucc_code,
			})
			.then((r) => {
			    var tradebook_data = r;
			    console.log(tradebook_data);
			    let data = {};
			    let dataPoints = {};
                tradebook_data.forEach(function(entry) {
                var myDate = new Date(entry.trade_date);
                var unixTimestamp = myDate.getTime();
                var unixTimestampInSeconds = Math.floor(unixTimestamp / 1000);
                var key = unixTimestampInSeconds;
                var value = parseInt(entry.tradebook_count);
                dataPoints[key] = value;
                });
                console.log(dataPoints);
                // data = {
                // dataPoints: dataPoints
                // };
//             let heatmap = new frappe.Chart('#myCanvas', {
// 			type: "heatmap",
// 			colors: ['#ebedf0', '#c0ddf9', '#73b3f3', '#3886e1', '#17459e'],
// 			domain: [0, 5, 10, 15, 25],
// 			countLabel: "Tradebook",
// 			data: data,
// 		});
			heatmap.update({ dataPoints: dataPoints });
			heatmap.draw();
			console.log(heatmap);
			});
	}
});

// frappe.ui.form.on('Customer', {
//     refresh: function(frm) {
//         // Your logic to get customer_ucc
//         var customer_ucc = cur_frm.doc.fsl_ucc_code;

//         // Fetch tradebook data for the customer
//         frappe.xcall("cs_bo.custom_codes.transaction_activity.get_trade_book_heatmap_data", { ucc: customer_ucc })
//             .then(function(tradebook_data) {
//                 // Assuming tradebook_data is an array of { trade_date, tradebook_count } objects

//                 // Extract tradebook counts
//                 var tradebookCounts = tradebook_data.map(function(entry) {
//                     return entry.tradebook_count;
//                 });

//                 // Set up color scale based on tradebook count range
//                 var minCount = Math.min(...tradebookCounts);
//                 var maxCount = Math.max(...tradebookCounts);

//                 // Define your color scale
//                 var colorScale = ['#ebedf0', '#c0ddf9', '#73b3f3', '#3886e1', '#17459e'];

//                 // Set up Frappe Charts configuration
//                 var heatmap = new frappe.Chart('#myCanvas', {
//                     type: "heatmap",
//                     colors: colorScale,
//                     domain: [minCount, maxCount],
//                     countLabel: "Tradebook Count",
//                     data: {},
// //                 });
// var dataPoint = {
//                     x: entry.ucc,
//                     y: entry.trade_date,
//                     value: parseInt(entry.tradebook_count),
//                 };

//                 // Assuming dataPoints is an array of data points with trade_date and tradebook_count properties
//                 var dataPoints = tradebook_data.map(function(entry) {
//                     return {
//                         x: entry.trade_date,
//                         y: customer_ucc,  // Assuming customer_ucc is the y-axis value
//                         value: entry.tradebook_count,
//                     };
//                 });

//                 // Update the heatmap with the data points
//                 heatmap.update({ dataPoints: dataPoints });
//             });
//     }
// });

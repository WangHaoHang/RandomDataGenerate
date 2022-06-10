"use strict";
function plotOne(x,y,figType,eleId,figTitle){
	var ele = echarts.init(document.getElementById(eleId));
	var position ={
		title:{
			text:figTitle,
			left:'center',
			textStyle:{
				fontFamily:"times new roman"
			}
		},
		xAxis:{
			data:x
		},
		yAxis:{},
		series:[
			{
				type:figType,
				data:y
			}
		]
	}
	ele.setOption(position);
}
/**
 * x,y1,type1,y2,type2,id,title
 */
function plotMul(){
	var len = arguments.length;
	var ele = echarts.init(document.getElementById(arguments[len-2]));
	var seriesDatas = new Array();
	var i = 1;
	while(i < len-2){
		var temp = new Object();
		temp.data = arguments[i];
		temp.type = arguments[i+1];
		seriesDatas.push(temp);
		i = i + 2;
	}
	console.log(seriesDatas);
	var position ={
		title:{
			text:arguments[len-1],
			left:'center',
			textStyle:{
				fontFamily:"times new roman"
			}
		},
		xAxis:{
			data:arguments[0]
		},
		yAxis:{},
		series:seriesDatas
	}
	ele.setOption(position);
}
/**
 * x,y1,type1,legend1,y2,type2,legend1,id,title
 */
function plotLegend(){
	var len = arguments.length;
	var ele = echarts.init(document.getElementById(arguments[len-2]));
	var seriesDatas = new Array();
	var i = 1;
	var legends = []
	while(i < len-2){
		var temp = new Object();
		temp.data = arguments[i];
		temp.type = arguments[i+1];
		temp.name = arguments[i+2];
		legends.push(arguments[i+2])
		seriesDatas.push(temp);
		i = i + 3;
	}
	// console.log(seriesDatas);
	var position ={
		title:{
			text:arguments[len-1],
			// left:'center',
			textStyle:{
				fontFamily:"times new roman"
			}
		},
		legend:{
			data:legends
		},
		xAxis:{
			data:arguments[0]
		},
		yAxis:{},
		series:seriesDatas
	}
	ele.setOption(position);
}
/**
 * x,[[y1,type1,legend1],[y2,type2,legend1]],id,title
 */
function plotLegendArray(){
	var len = arguments.length;
	var ele = echarts.init(document.getElementById(arguments[len-2]));
	var tuple = arguments[1];
	var tuple_len = tuple.length;
	var seriesDatas = new Array();
	var i = 0;
	var legends = []
	while(i < tuple_len){
		var temp = new Object();
		temp.data = tuple[i][0];
		temp.type = tuple[i][1];
		temp.name = tuple[i][2];
		legends.push(tuple[i][2])
		seriesDatas.push(temp);
		i = i+1;
	}
	// console.log(seriesDatas);
	var position ={
		title:{
			text:arguments[len-1],
			// left:'center',
			textStyle:{
				fontFamily:"times new roman"
			}
		},
		legend:{
			data:legends
		},
		xAxis:{
			data:arguments[0]
		},
		yAxis:{},
		series:seriesDatas
	}
	ele.setOption(position);
}
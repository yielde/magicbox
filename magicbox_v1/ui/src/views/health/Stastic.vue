<!--
 * @Author: Galen Tong
 * @Date: 2022-08-19 09:44:48
 * @LastEditTime: 2022-08-19 23:35:37
 * @Description: 
-->
<template>
	<div>
		<el-card class="box-card">
			<highcharts :options="stasticData"></highcharts>
		</el-card>
	</div>
</template>

<script>
	export default {
		name: "Stastic",
		data() {
			return {
				stasticData: {
					chart: {
						type: "line",
					},
					title: {
						text: "时间间隔",
					},
					subtitle: {
						text: "距离上个开始日间隔的天数",
					},
					xAxis: {
						type: "category",
                        categories:['2021-07-15', '2022-07-23', '2022-08-02', '2022-08-04'],
						labels: {
							rotation: 90,
						},
					},
					yAxis: {
						min: 0,
						title: {
							text: "天数",
						},
					},
					tooltip: {
						pointFormat: "距离上次疼痛间隔<b>{point.y} 天</b>",
					},
					series: [
						{
							data: [
                                0,373,10,2
							],
						},
					],
				},
			};
		},
	};
</script>

<style>
</style>
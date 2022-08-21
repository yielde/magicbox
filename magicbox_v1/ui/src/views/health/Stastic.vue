<!--
 * @Author: Galen Tong
 * @Date: 2022-08-19 09:44:48
 * @LastEditTime: 2022-08-21 00:25:53
 * @Description: 
-->
<template>
	<div class="stastic-box">
		<el-card class="box-card">
			<highcharts :options="stasticDataLine"></highcharts>
		</el-card>
		<el-card class="box-card">
			<highcharts :options="stasticDataColumn"></highcharts>
		</el-card>
	</div>
</template>

<script>
	export default {
		name: "Stastic",
		data() {
			return {
				stasticDataLine: {
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
						categories: [],
						labels: {
							rotation: 300,
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
							name: "统计折线图",
							data: [],
						},
					],
				},
				stasticDataColumn: {
					chart: {
						type: "column",
					},
					title: {
						text: "时间间隔",
					},
					subtitle: {
						text: "距离上个开始日间隔的天数",
					},
					xAxis: {
						type: "category",
						categories: [],
						labels: {
							rotation: 300,
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
							name: "统计柱状图",
							data: [],
						},
					],
				},
			};
		},
		created() {
			this.axisPatch();
		},
		methods: {
			axisPatch() {
				this.axios
					.get("/health/stastic/")
					.then((res) => {
						if (res.data.code === 0) {
							this.stasticDataColumn.xAxis.categories = JSON.parse(
								JSON.stringify(res.data.data.axis_key)
							);
							this.stasticDataColumn.series[0].data = JSON.parse(
								JSON.stringify(res.data.data.axis_value)
							);
							this.stasticDataLine.xAxis.categories = JSON.parse(
								JSON.stringify(res.data.data.axis_key)
							);
							this.stasticDataLine.series[0].data = JSON.parse(
								JSON.stringify(res.data.data.axis_value)
							);
						}
					})
					.catch((err) => {
						this.$message.error(err);
					});
			},
		},
	};
</script>

<style scop>
	.box-card {
		margin-bottom: 15px;
	}
	.stastic-box {
		margin: 15px;
	}
</style>
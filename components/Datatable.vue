<template lang="pug">
.data-table
  table.data-table-table
    thead
      tr
        slot(name="prependHead")
        th(v-for="col in cols" :key="col.name"
          :style="col.getHeadStyle && col.getHeadStyle({col})"
          :class="col.getHeadClass && col.getHeadClass({col})"
        )
          slot(name="prependHeadCell" :col="col")
          slot(:col="col") {{col.text}}
          slot(name="appendHeadCell" :col="col")
        slot(name="appendHead")
    tbody
      slot(name="prependBody")
      tr(v-for="(row, index) in rows" :key="row[rowKey] || index"
        :style="getRowStyle && getRowStyle({row})"
        :class="getRowClass && getRowClass({row})"
      )
        slot(name="prependRow" :row="row")
        td(v-for="col in cols" :key="col.name"
          :style="col.getCellStyle && col.getCellStyle({value: row[col.name], col, row})"
          :class="col.getCellClass && col.getCellClass({value: row[col.name], col, row})"
        )
          slot(name="prependCell" :row="row" :col="col" :value="row[col.name]")
          slot(name="cell" :row="row" :col="col" :value="row[col.name]") {{row[col.name]}}
          slot(name="appendCell" :row="row" :col="col" :value="row[col.name]")
        slot(name="appendRow" :row="row")
      slot(name="appendBody")
  .space
  el-pagination.pull-right(:total="50" :page-size="10")
  .clearfix
</template>

<script>
export default {
  // components: {},
  props: {
    cols: {},
    rows: {},
    rowKey: {},
    getRowStyle: {type: Function},
    getRowClass: {type: Function},
  },
  data() {
    return {}
  },
  // computed: {},
  watch: {},
  // methods: {},
  // created() {},
  // mounted() {},
}
</script>

<style lang="scss">
.data-table{
  overflow: auto;
}
.data-table-table{
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  font-size: 12px;
  tbody{
   tr{
     &:nth-of-type(odd) {
      background-color: #f9f9f9;
    }
    &:hover{
      background-color: #f5f5f5;
    }
   }
  }

  th, td{
    padding: 10px 15px;
  }
  thead{
    color: #fff;
    background: #434343;
  }
}
</style>

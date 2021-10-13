<template>
  <div class="sketch_container">
    <h1 v-if="title!=null">{{ title }}</h1>
    <div class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100 canvas_loader_container">
      <PaintCanvasLoader />
    </div>
  </div>
</template>

<script>
import PaintCanvasLoader from './Canvas/PaintCanvasLoader.vue'

export default {
  name: 'root-view',
  props: {
    title: String
  },
  components: { PaintCanvasLoader }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.sketch_container{
  position: absolute;
  width:100%;
  height:100%;
  top:0;
}
.canvas_loader_container{
  position: absolute;
  width:100%;
  height:100%;
}
</style>

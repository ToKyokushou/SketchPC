<template>
  <div class="viewport"></div>
</template>

<script>
import { mapMutations, mapActions, mapGetters } from 'vuex'

export default {
  name: 'ViewPort',
  props: ['points', 'modalFile'],
  data () {
    return {
      height: 0
    }
  },
  methods: {
    ...mapGetters(['PNG_DATA']),
    ...mapMutations(['RESIZE', 'GET_PNG', 'RENDER_MODEL']),
    ...mapActions(['INIT', 'ANIMATE']),
    transCanvasData (val) {
      // console.log(val)
      // let canvas = this.GET_PNG()
      // console.log(canvas)
      let canvasData = null
      canvasData = this.PNG_DATA()
      return canvasData
    },
    renderModel () {
      // only show 3D model here
      console.log('start render new model 1')
      this.RENDER_MODEL()
    }
  },
  mounted () {
    this.INIT({
      width: this.$el.offsetWidth,
      height: this.$el.offsetHeight,
      el: this.$el,
      points: this.points,
      modalFile: this.modalFile
    }).then(() => {
      this.ANIMATE()
      window.addEventListener(
        'resize',
        () => {
          // console.log(this.$el.offsetWidth)
          // console.log(this.$el.offsetHeight)
          this.RESIZE({
            width: this.$el.offsetWidth,
            height: this.$el.offsetHeight
          })
        },
        true
      )
    })
  }
}
</script>

<style>
.viewport {
  height: 100%;
  width: 100%;
}
</style>

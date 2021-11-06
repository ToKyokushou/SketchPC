<template>
  <div class="loader_container">
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
    />
    <div class="md-layout md-gutter action-buttons-part">
      <div class="md-layout-item">
        <md-button
          id="draw"
          class="md-icon-button md-primary action_button"
          v-on:click="onDraw"
        >
          <md-icon class="md-size-2x">border_color</md-icon>
        </md-button>
        <md-button
          id="erase"
          class="md-icon-button md-primary action_button"
          v-on:click="onErase"
        >
          <md-icon class="md-size-2x">auto_fix_normal</md-icon>
        </md-button>
        <md-button
          id="undo"
          class="md-icon-button md-primary action_button"
          v-on:click="onUndo"
        >
          <md-icon class="md-size-2x">undo</md-icon>
        </md-button>
        <md-button
          id="redo"
          class="md-icon-button md-primary action_button"
          v-on:click="onRedo"
        >
          <md-icon class="md-size-2x">redo</md-icon>
        </md-button>
        <md-button
          id="clear"
          class="md-icon-button md-primary action_button"
          v-on:click="onClearCanvas"
        >
          <md-icon class="md-size-2x">clear</md-icon>
        </md-button>
        <!-- <md-button
          id="draw"
          class="md-icon-button md-primary action_button"
          v-on:click="onAddLayer"
        >
          <md-icon class="md-size-2x">layers</md-icon>
        </md-button> -->
        <!-- TODO: remove layer -->
        <!-- <md-button
          id="draw"
          class="md-icon-button md-primary"
          v-on:click="onRemoveLayer"
        >
          <md-icon class="md-size-2x">layers_clear</md-icon>
        </md-button> -->
        <md-button
          class="md-icon-button md-primary"
          id="save"
          v-on:click="onSave"
        >
          <md-icon class="md-size-2x">done</md-icon>
        </md-button>
      </div>
    </div>
    <div class="container">
      <PaintCanvas
        ref="paintCanvas"
        :mode="mode"
        :brushColor="brushColor"
        :brushSize="brushSize"
        :eraserSize="eraserSize"
      />
    </div>
    <!-- <div>
      <div>
        <label>Brush size:</label>
        <input type="range" v-model.number="brushSize" :min="0" :max="36" />
        <label>Eraser size:</label>
        <input type="range" v-model.number="eraserSize" :min="0" :max="50" />
      </div>
    </div> -->
  </div>
</template>

<script>
import PaintCanvas from './PaintCanvas.vue'
export default {
  name: 'paint-canvas-loader',
  components: { PaintCanvas },
  props: {},
  data: () => ({
    mode: '',
    brushColor: '',
    brushSize: 3,
    eraserSize: 20,
    defaultMode: 'brush',
    defaultBrushColor: '#000000',
    currentAction: 'draw'
  }),
  mounted: function () {
    // 初期化
    this.init()
    // this.setCanvasBackwrite(
    //   '/home/du/iwaitPro/sketch-ui/src/assets/img.png'
    // )
    // for : onAddLayer()
  },
  methods: {
    init: function () {
      this.mode = this.defaultMode
      this.brushColor = this.defaultBrushColor
      this.onAction('draw')
      this.currentAction = 'draw'
      // console.log(this.$refs)
    },
    onDraw: function () {
      this.mode = 'brush'
      this.onAction('draw')
    },
    onErase: function () {
      this.mode = 'eraser'
      this.onAction('erase')
    },
    onClearCanvas: function () {
      this.$refs.paintCanvas.onClearCanvas()
      this.init()
    },
    onUndo: function () {
      this.$refs.paintCanvas.undo()
    },
    onRedo: function () {
      this.$refs.paintCanvas.redo()
    },
    onAction: function (targetAction) {
      if (this.currentAction !== targetAction) {
        let activatedButton = document.getElementById(this.currentAction)
        activatedButton.classList.remove('md-accent')
        activatedButton.classList.add('md-primary')
        let targetButton = document.getElementById(targetAction)
        targetButton.classList.remove('md-primary')
        targetButton.classList.add('md-accent')
        this.currentAction = targetAction
      } else {
        let targetButton = document.getElementById(targetAction)
        targetButton.classList.remove('md-primary')
        targetButton.classList.add('md-accent')
      }
    },
    onAddLayer: function () {
      this.$refs.paintCanvas.addLayer()
    },
    onRemoveLayer: function () {
      this.$refs.paintCanvas.removeLayer()
    },
    onSave: function () {
      let imgUrl = this.$refs.paintCanvas.onSave()
      // console.log('imgUrl', imgUrl)
      this.$emit('getSketchValue', imgUrl)
    },
    setCanvasBackwrite: function (imgSrc) {
      this.$refs.paintCanvas.setCanvas(imgSrc)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.md-field {
  max-width: 50px;
}
.md-icon-button {
  width: 72px;
  height: 72px;
}
.container {
  /* margin: 10px 120px; */
  width: 100%;
  height: 100%;
  /* opacity: 0.5; */
}
.action-buttons-part {
  margin: 0px;
  position: absolute;
  left: -124px;
}
.loader_container {
  width: 100%;
  height: 100%;
}
.action_button {
  display: block;
}
</style>

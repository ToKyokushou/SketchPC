<template>
  <div class="paint_canvas">
    <div
      ref="container"
      class="container"
    />
    <!-- <div
      ref="layers_previewer"
      class="md-layout-item md-medium-size-100 md-xsmall-size-100 md-size-100"
    >
    </div> -->
  </div>
</template>

<script>
import Konva from 'konva'
// import Canvas2Image from 'canvas2image'
// import axios from 'axios'
export default {
  name: 'paint-canvas',
  props: {
    mode: {
      type: String,
      default: ''
    },
    brushColor: {
      type: String,
      default: ''
    },
    backgroundImage: {
      type: String,
      default: ''
    }
  },
  data: () => ({
    stage: null,
    context: null,
    canvasGroup: [],
    drawingLayer: null,
    lastPointerPosition: {},
    isPaint: false,
    undoStack: [],
    redoStack: [],
    paint_history: [],
    pen_history: [],
    layerCount: 1,
    layerActive: 0
    // width: 720,
    // height: 720
    // width: this.$refs.container.offsetWidth,
    // height: this.$refs.container.offsetHeight
  }),
  mounted: function () {
    var container = this.$refs.container
    this.width = container.offsetWidth
    this.height = container.offsetHeight
    this.stage = new Konva.Stage({
      container,
      width: this.width,
      height: this.height
    })
    this.drawingLayer = new Konva.Layer()
    this.stage.add(this.drawingLayer)

    this.canvasGroup.push(this.drawingScope())
    // this.previewLayer()
  },
  methods: {
    drawingScope: function () {
      let canvas = document.createElement('canvas')
      canvas.id = 'sketch_canvas'
      canvas.ref = 'canvas_' + this.layerCount
      canvas.width = this.width
      canvas.height = this.height
      let drawingScope = new Konva.Image({
        image: canvas
      })
      this.drawingLayer.add(drawingScope)
      this.stage.draw()

      this.context = canvas.getContext('2d')
      this.context.strokeStyle = this.brushColor
      this.context.lineJoin = 'round'
      this.context.lineWidth = 3

      // add event
      drawingScope.on('mousedown', this.mousedown)
      this.stage.addEventListener('mouseup', this.mouseup)
      this.stage.addEventListener('mousemove', this.mousemove)
      drawingScope.on('touchstart', this.mousedown)
      this.stage.addEventListener('touchend', this.mouseup)
      this.stage.addEventListener('touchmove', this.mousemove)

      return canvas
    },
    mousedown: function () {
      this.isPaint = true
      this.lastPointerPosition = this.stage.getPointerPosition()
      this.undoStack.push({
        layer: this.layerActive,
        content: this.context.getImageData(0, 0, this.width, this.height)
      })
    },
    mouseup: function () {
      this.isPaint = false

      //   axios
      //     .post('https://www.ultratks.live/api/sketch/stroke/save_stroke', {
      //       request_type: 'save_stroke',
      //       pen_history: this.pen_history
      //     })
      //     .then(function (response) {
      //       if (response.data.response_type === 'save_confirmed') {
      //         console.log('save confirmed')
      //       } else {
      //         throw Error('Failed. Please contact the server admin.')
      //       }
      //     })
      //     .catch(function (error) {
      //       console.log(error)
      //       self.operation = 'Confirm'
      //     })
      this.pen_history = []
    },
    mousemove: function () {
      if (!this.isPaint) {
        return
      }
      if (this.isTargetMode('brush')) {
        this.context.globalCompositeOperation = 'source-over'
      }
      if (this.isTargetMode('eraser')) {
        this.context.globalCompositeOperation = 'destination-out'
      }

      // get image data before paint
      // let image_data_before = this.context.getImageData(
      //   0,
      //   0,
      //   this.width,
      //   this.height
      // ).data;

      this.context.beginPath()

      let localPos = {
        x: 0,
        y: 0
      }

      localPos.x = this.lastPointerPosition.x
      localPos.y = this.lastPointerPosition.y
      // eslint-disable-next-line camelcase
      let last_pos = { x: localPos.x, y: localPos.y }

      this.context.moveTo(localPos.x, localPos.y)

      let pos = this.stage.getPointerPosition()
      localPos.x = pos.x
      localPos.y = pos.y

      this.context.lineTo(localPos.x, localPos.y)
      this.context.closePath()
      this.context.stroke()
      this.drawingLayer.draw()

      this.lastPointerPosition = pos

      // get image data before paint
      // let image_data_after = this.context.getImageData(
      //   0,
      //   0,
      //   this.width,
      //   this.height
      // ).data;

      // save history as json
      // this.paint_history.push({
      //   layer: this.layerActive,
      //   before: image_data_before,
      //   after: image_data_after
      // });
      this.pen_history.push({
        layer: this.layerActive,
        last_pen_position: last_pos,
        now_pen_position: { x: pos.x, y: pos.y }
      })
    },
    onClearCanvas: function () {
      this.undoStack.push({
        layer: this.layerActive,
        content: this.context.getImageData(0, 0, this.width, this.height)
      })
      this.context.globalCompositeOperation = 'destination-out'
      this.context.fillRect(0, 0, this.stage.width(), this.stage.height())
      this.drawingLayer.draw()
    },
    isTargetMode: function (targetMode) {
      return this.mode === targetMode
    },
    undo: function () {
      if (this.undoStack.length <= 0) {
        return
      }

      this.redoStack.push({
        layer: this.layerActive,
        content: this.context.getImageData(0, 0, this.width, this.height)
      })

      this.context.putImageData(this.undoStack.pop().content, 0, 0)
      this.drawingLayer.draw()
    },
    redo: function () {
      if (this.redoStack.length <= 0) {
        return
      }

      this.undoStack.push({
        layer: this.layerActive,
        content: this.context.getImageData(0, 0, this.width, this.height)
      })

      this.context.putImageData(this.redoStack.pop().content, 0, 0)
      this.drawingLayer.draw()
    },
    addLayer: function () {
      this.canvasGroup.push(this.drawingScope())
      this.layerCount++
      this.layerActive++
    //   this.previewLayer()
    },
    removeLayer: function () {
      this.drawingLayer.get(this.layerCount).destroy()
      this.drawingLayer.draw()
      this.layerCount--
      this.layerActive--
    //   this.previewLayer()
    },
    previewLayer: function () {
      // eslint-disable-next-line camelcase
      let layer_previewer = this.$refs.layers_previewer
      while (layer_previewer.firstChild) {
        layer_previewer.removeChild(layer_previewer.firstChild)
      }
      for (let idx = 0; idx < this.canvasGroup.length; idx++) {
        // var image = new Image();
        // image.id = "preview_layer_" + idx;
        // image.src = this.canvasGroup[idx].toDataURL();

        // eslint-disable-next-line camelcase
        let layer_preview_button = document.createElement('button')
        layer_preview_button.id = 'btn_layer_' + idx
        layer_preview_button.innerHTML = 'layer_' + idx
        layer_previewer.onclick = this.onBtnLayerClick

        layer_previewer.appendChild(layer_preview_button)
      }
    },
    onBtnLayerClick: function (e) {
      this.layerActive = Number(e.srcElement.id.split('_')[2])
    },
    onSave: function () {
      console.log(this.canvasGroup)
      //   let oCanvas = this.canvasGroup[0]
      //   Canvas2Image.saveAsPNG(oCanvas, true)

      let dlLink = document.createElement('a')
      let oCanvas = this.canvasGroup[0]
      let dataUrl = oCanvas.toDataURL({format: 'image/png'})
      dlLink.download = 'sketchImg'
      dlLink.href = dataUrl
      dlLink.click()

    //   axios
    //     .post('https://www.ultratks.live/api/sketch/stroke/save_history', {
    //       request_type: 'save_history'
    //     })
    //     .then(function (response) {
    //       if (response.data.response_type === 'save_confirmed') {
    //         console.log('save confirmed')
    //       } else {
    //         throw Error('Failed. Please contact the server admin.')
    //       }
    //     })
    //     .catch(function (error) {
    //       console.log(error)
    //       self.operation = 'Confirm'
    //     })
    }
  },
  watch: {
    brushColor: function () {
      this.context.strokeStyle = this.brushColor
    },
    layerActive: function () {
      for (let idx = 0; idx < this.canvasGroup.length; idx++) {
        let canvas = this.canvasGroup[idx]
        let ctx = canvas.getContext('2d')

        let imageData = ctx.getImageData(0, 0, this.width, this.height)
        let pixels = imageData.data
        if (idx === this.layerActive) {
          // TOP LAYER COLOR: BLACK

          for (let i = 0; i < pixels.length; i += 4) {
            // Is this pixel *gray* ?
            if (pixels[i] === 127) {
              pixels[i] = 0
              pixels[i + 1] = 0
              pixels[i + 2] = 0
            }
          }
        } else {
          // OTHER LAYERS COLOR: GRAY

          for (let i = 0; i < pixels.length; i += 4) {
            // Is this pixel *black* ?
            if (pixels[i] === 0) {
              pixels[i] = 127
              pixels[i + 1] = 127
              pixels[i + 2] = 127
            }
          }
        }
        ctx.putImageData(imageData, 0, 0)
        this.drawingLayer.draw()
      }
      this.context = this.canvasGroup[this.layerActive].getContext('2d')
      // this.context.strokeStyle = this.brushColor;
      this.context.strokeStyle = this.brushColor
      this.context.lineJoin = 'round'
      this.context.lineWidth = 3
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  border: 3px solid #000;
  /* max-width: 720px; */
  align-items: center;
  text-align: center;
  display: inline-block;
  width: 100%;
  height: 100%
}
.paint_canvas{
    width:100%;
    height:100%;
}
</style>

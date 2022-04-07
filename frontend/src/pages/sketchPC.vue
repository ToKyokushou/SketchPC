<template>
  <div class="container">
    <!-- <div class="header">March Score ( 90 ) Points</div> -->
    <div class="header">3D Modal Search and Generation System</div>
    <el-row :gutter="10">
      <el-col :span="3">
        <div class="left_part">
          <el-button
            class="left_part_button"
            type="primary"
            plain
            @click="importFile"
          >
            Import
          </el-button>
          <input
            type="file"
            id="files"
            ref="refFile"
            style="display: none"
            @change="fileLoad"
          />
          <!-- <upload></upload> -->
          <el-button
            class="left_part_button"
            type="primary"
            plain
            @click="displaySketch"
          >
            {{ sketchReFresh ? "Cancel" : "Draw" }}
          </el-button>
          <el-button
            class="left_part_button"
            type="primary"
            plain
            @click="confirmExportResult"
          >
            Export
          </el-button>
          <!-- <el-button type='primary' plain>
                        Clear
                    </el-button>
                    <el-button type='primary' plain>
                        Reset
                    </el-button>
                    <el-button type='primary' plain>
                        Save
                    </el-button> -->
        </div>
      </el-col>
      <el-col :span="18">
        <div class="main_part">
          <viewport
            v-if="reFresh"
            ref="canvasData"
            :points="points"
            :modalFile="modalFile"
          ></viewport>
          <rootview
            v-if="sketchReFresh"
            ref="canvasView"
            v-on:getSketchData="getSketchData"
          ></rootview>
        </div>
      </el-col>
      <el-col :span="3">
        <div class="right_part">
          <el-button
            class="right_part_button"
            type="primary"
            plain
            @click="openShell"
          >
            3D Search
          </el-button>
          <!-- <el-button type="primary" plain @click="search3D">
            3D Search
          </el-button> -->
          <el-button
            class="right_part_button"
            type="primary"
            plain
            @click="getPng"
          >
            Transform
          </el-button>
          <el-button
            class="right_part_button"
            type="primary"
            plain
            @click="iteration"
          >
            ICP
          </el-button>
          <!-- <el-button type="primary" plain @click="openShell"> Shell </el-button> -->
          <!-- <div class="right_bottom">
            <p>
              X
              <el-input></el-input>
            </p>
            <p>
              Y
              <el-input></el-input>
            </p>
            <p>
              Z
              <el-input></el-input>
            </p>
          </div> -->
          <div class="right_bottom">
            <panel ref="controlPanel"></panel>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// import upload from '../components/upload.vue'
import ViewPort from '../components/ViewPort.vue'
import RootView from '../components/RootView.vue'
import ControlPanel from '../components/ControlPanel.vue'

export default {
  name: 'sketchPC',
  data () {
    return {
      points: this.points,
      reFresh: false,
      sketchReFresh: false,
      sketchData: null,
      modalFile: null,
      objFile: null,
      icpObjFile: null
    }
  },
  watch: {
    'points': function (val) {
      this.reFresh = false
      this.$nextTick(() => {
        this.reFresh = true
      })
    },
    'modalFile': function (val) {
      console.log('modalFile change')
      // let filename = val
      // filename = filename.substring(55, 61)
      // this.modalFile = val
      // console.log(val)
      this.reFresh = false
      this.sketchReFresh = false
      this.$nextTick(() => {
        this.reFresh = true
      })
    }
  },
  components: {
    //     upload
    viewport: ViewPort,
    rootview: RootView,
    panel: ControlPanel
  },
  methods: {
    importFile () {
      this.modalFile = null
      document.getElementById('files').click()
    },
    fileLoad (points) {
      //   let points
      let $ = this
      const selectedFile = this.$refs.refFile.files[0]
      if (selectedFile) {
        let reader = new FileReader()
        reader.readAsText(selectedFile)
        reader.onload = function () {
          // console.log(this.result)
          // points = this.result
          // $.points = 'hahahahaha'
          $.$data.displayPC = true
          $.$data.points = this.result
        }
      }
    },
    displaySketch () {
      // eslint-disable-next-line eqeqeq
      if (this.sketchReFresh == false) {
        this.sketchReFresh = true
      } else {
        this.sketchReFresh = false
      }
    },
    // search3D () {
    //   console.log('start searching 3D content')
    //   let postData = {
    //     // 'imgUrl': 'img/sketchImg.png'
    //     'imgUrl': this.sketchData
    //   }
    //   // console.log('sketchData', postData.imgUrl)
    //   this.axios.post(
    //     'http://localhost:5000/search',
    //     postData
    //   ).then(
    //     res => {
    //       console.log(res.data)
    //     }
    //   ).catch(
    //     res => {
    //       console.log(res.data)
    //     }
    //   )
    // },
    getSketchData (data) {
      //   console.log('sketchData', data)
      this.sketchData = data
    },
    openShell () {
      let $ = this
      console.log('execute the command statement')
      let postData = {
        'imgUrl': this.sketchData
      }
      this.axios.post(
        'http://localhost:5000/shell',
        postData
      ).then(
        res => {
          console.log(res.data)
          let filePath = res.data
          filePath = filePath.substring(45, 52)
          console.log(filePath)
          $.objFile = filePath
          // $.objFile = '/D00107'
          $.modalFile = $.objFile
          console.log($.modalFile)
          this.resetControlPanel()
          // $.objFile = filePath
          // if ($.objFile === $.modalFile) {
          //   alert('The same model was retrieved')
          // } else {
          //   $.modalFile = $.objFile
          //   console.log($.modalFile)
          //   this.resetControlPanel()
          // }
        }
      ).catch(
        res => {
          console.log(res.data)
        }
      )
    },
    getPng () {
      let $ = this
      // this.$refs.controlPanel.toggleAxisLines()
      let canvasData = this.$refs.canvasData.transCanvasData('test get png')
      // console.log(canvasData)
      let postData = {
        'canvasData': canvasData
      }
      this.axios.post(
        'http://localhost:5000/trans',
        postData
      ).then(
        res => {
          // console.log(res.data)
          // $.$refs.canvasView.importPng('/home/du/iwaitPro/SketchPC/backend/3.txt')
          $.$refs.canvasView.importPng()
        }
      ).catch(
        res => {
          console.log(res.data)
        }
      )
    },
    iteration () {
      let $ = this
      if ($.objFile) {
        $.modalFile = $.objFile
      }
      let postData = {
        'target': $.$refs.refFile.files[0].name,
        'original': $.modalFile
      }
      console.log(postData)
      this.axios.post(
        'http://localhost:5000/iteration',
        postData
      ).then(
        res => {
          console.log(res.data)
          $.icpObjFile = res.data
          $.modalFile = $.icpObjFile
          this.resetControlPanel()
        }
      ).catch(
        res => {
          console.log(res.data)
        }
      )
    },
    confirmExportResult () {
      console.log('download start')
      let link = document.createElement('a')
      link.href = '/static/threeDs/' + this.modalFile + '.obj'
      console.log(link.href)
      link.click()
      URL.revokeObjectURL(link.href)
    },
    resetControlPanel () {
      this.$refs.controlPanel.resetControlPanle()
    }
  }
}
</script>

<style scoped>
.container {
  height: 100%;
  /* background: red; */
}
.header {
  font-weight: bold;
  text-align: center;
  height: 30px;
  line-height: 30px;
}
.left_part,
.right_part {
  width: 100px;
  /* background: cornflowerblue; */
  border-radius: 10px;
}
.el-button {
  /* display: block; */
  width: 100px;
  margin: 5px 0;
}
.el-row {
  width: 100%;
  height: calc(100% - 50px);
  /* background: green; */
}
.el-col {
  height: 100%;
  /* background: yellow; */
}
.main_part {
  margin: 5px 0;
  background: #d9ecff;
  /* background: #fff; */
  /* min-height:50px; */
  height: 100%;
  position: relative;
}
.right_bottom {
  position: fixed;
  bottom: 0px;
  width: 300px;
  border: 1px solid #ddd;
  margin-bottom: 15px;
  padding: 5px;
  border-radius: 5px;
}
.el-input {
  width: 78%;
}
.left_part_button {
  margin-left: 77px;
}
.right_part_button {
  margin-left: 77px;
}
</style>

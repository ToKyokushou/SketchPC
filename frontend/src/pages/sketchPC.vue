<template>
    <div class='container'>
        <div class='header'>
            March Score ( 90 ) Points
        </div>
        <el-row :gutter='10'>
            <el-col :span='3'>
                <div class='left_part'>
                    <el-button type='primary' plain @click="importFile">
                        Import
                    </el-button>
                    <input type="file" id="files" ref='refFile' style='display:none' @change="fileLoad">
                    <!-- <upload></upload> -->
                    <el-button type='primary' plain @click="displaySketch">
                        Draw
                    </el-button>
                    <el-button type='primary' plain>
                        Clear
                    </el-button>
                    <el-button type='primary' plain>
                        Reset
                    </el-button>
                    <el-button type='primary' plain>
                        Save
                    </el-button>
                </div>
            </el-col>
            <el-col :span='18'>
                <div class='main_part'>
                    <viewport v-if="reFresh" :points="points"></viewport>
                    <rootview v-if="sketchReFresh" v-on:getSketchData='getSketchData' />
                </div>
            </el-col>
            <el-col :span='3'>
                <div class='right_part'>
                    <el-button type='primary' plain @click="search3D">
                        3D Search
                    </el-button>
                    <el-button type='primary' plain>
                        Transform
                    </el-button>
                    <div class='right_bottom'>
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

export default {
  name: 'sketchPC',
  data () {
    return {
      points: this.points,
      reFresh: false,
      sketchReFresh: false,
      sketchData: null
    }
  },
  watch: {
    'points': function (val) {
      this.reFresh = false
      this.$nextTick(() => {
        this.reFresh = true
      })
    }
  },
  components: {
  //     upload
    viewport: ViewPort,
    rootview: RootView
  },
  methods: {
    importFile () {
      document.getElementById('files').click()
    },
    fileLoad (points) {
    //   let points
      let $ = this
      const selectedFile = this.$refs.refFile.files[0]
      let reader = new FileReader()
      reader.readAsText(selectedFile)
      reader.onload = function () {
        // console.log(this.result)
        // points = this.result
        // $.points = 'hahahahaha'
        $.$data.displayPC = true
        $.$data.points = this.result
      }
    },
    displaySketch () {
      // eslint-disable-next-line eqeqeq
      if (this.sketchReFresh == false) {
        this.sketchReFresh = true
      }
    },
    search3D () {
      console.log('start searching 3D content')
      let postData = {
        // 'imgUrl': 'img/sketchImg.png'
        'imgUrl': this.sketchData
      }
      // console.log('sketchData', postData.imgUrl)
      this.axios.post(
        'http://localhost:5000/search',
        postData
      ).then(
        res => {
          console.log(res.data)
        }
      ).catch(
        res => {
          console.log(res.data)
        }
      )
    },
    getSketchData (data) {
    //   console.log('sketchData', data)
      this.sketchData = data
    }
  }
}
</script>

<style scoped>
.container{
    height: 100%;
    /* background: red; */
}
.header{
    font-weight: bold;
    text-align: center;
    height: 30px;
    line-height:30px;
}
.left_part, .right_part{
    width:100px;
    /* background: cornflowerblue; */
    border-radius: 10px;
}
.el-button{
    /* display: block; */
    width: 100px;
    margin: 5px 0;
}
.el-row{
    width:100%;
    height: calc(100% - 50px);
    /* background: green; */
}
.el-col{
    height:100%;
    /* background: yellow; */
}
.main_part{
    margin: 5px 0;
    background: #d9ecff;
    /* min-height:50px; */
    height:100%;
    position: relative;
}
.right_bottom{
    position: fixed;
    bottom: 0px;
}
.el-input{
    width: 78%;
}
</style>

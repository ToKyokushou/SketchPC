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
                    <el-button type='primary' plain>
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
                    <!-- {{points}} -->
                    <viewport></viewport>
                </div>
            </el-col>
            <el-col :span='3'>
                <div class='right_part'>
                    <el-button type='primary' plain>
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

export default {
  name: 'sketchPC',
  components: {
  //     upload
    viewport: ViewPort
  },
  methods: {
    importFile () {
      document.getElementById('files').click()
    },
    fileLoad () {
    //   let points
      const selectedFile = this.$refs.refFile.files[0]
      let reader = new FileReader()
      reader.readAsText(selectedFile)
      reader.onload = function () {
        // console.log(this.result)
        // points = this.result
      }
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
}
.right_bottom{
    position: fixed;
    bottom: 0px;
}
.el-input{
    width: 78%;
}
</style>

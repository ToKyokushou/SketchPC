<template>
<div>
<el-upload
     drag
    :limit="1"
     action="https://jsonplaceholder.typicode.com/posts/"
     ref="upload"
     accept=".json"
     :file-list="fileList"
     :on-success="onSuccess"
     :on-remove="onRemove">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">上传json文件，且只能上传 1 个文件</div>
 </el-upload>
 <el-button type="primary" @click="save">
     submit
 </el-button>
</div>
</template>

<script>
export default {
  name: 'upload',
  data () {
    return {
      fileList: [],
      uploadData: []
    }
  },
  methods: {
    onSuccess (res, file, fileList) {
      let reader = new FileReader()
      reader.readAsText(file.raw)
      reader.onload = (e) => {
        this.uploadData = []
        this.uploadData = JSON.parse(e.target.result)
      }
    },
    onRemove (file) {
      this.fileList = []
    },
    save () {
      // 把数据发送给 父元素
      this.$emit('uploadParent', this.uploadData)
    }
  }
}
</script>

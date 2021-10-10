<template>
    <div class='container'>
        <div class='header'>
            Sketch Point Clouds System
        </div>
        <el-row :gutter='10'>
            <el-col :span='3'>
                <div class='left_part'>
                    <el-button type='primary' plain>
                        Import
                    </el-button>
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
                    main part
                </div>
            </el-col>
            <el-col :span='3'>
                <div class='right_part'>
                    right part
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
  name: 'sketchPC'
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
.left_part{
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
    background: #409eff;
    /* min-height:50px; */
    height:100%;
}
</style>

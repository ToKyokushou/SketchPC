import Vue from 'vue'
import Vuex from 'vuex'

import {
  Scene,
  TrackballControls,
  PerspectiveCamera,
  WebGLRenderer,
  Color,
  // FogExp2,
  // CylinderBufferGeometry,
  // MeshPhongMaterial,
  // Mesh,
  DirectionalLight,
  AmbientLight,
  LineBasicMaterial,
  Geometry,
  Vector3,
  Line,
  // ThreeMFLoader,
  Points,
  PointsMaterial,
  // MTLLoader,
  OBJLoader,
  // BoxGeometry,
  // MeshBasicMaterial,
  Mesh,
  // MeshBasicMaterial,
  // MeshLambertMaterial,
  // MeshStandardMaterial,
  MeshNormalMaterial
  // Mesh,
  // ConvexGeometry,
  // MeshLambertMaterial,
  // BackSide,
  // FrontSide
  // Box3,
  // MeshBasicMaterial
} from 'three-full'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    width: 0,
    height: 0,
    camera: null,
    controls: null,
    scene: null,
    renderer: null,
    axisLines: [],
    pyramids: [],
    modalData: []
  },
  getters: {
    CAMERA_POSITION: state => {
      return state.camera ? state.camera.position : null
    },
    PNG_DATA: state => {
      var link = document.createElement('a')
      // 通过超链接herf属性，设置要保存到文件中的数据
      var canvas = state.renderer.domElement
      // console.log(canvas)
      // 获取canvas对象
      link.href = canvas.toDataURL('image/png')
      // console.log(link.href)
      return link.href
    }
  },
  mutations: {
    SET_VIEWPORT_SIZE (state, { width, height }) {
      state.width = width
      state.height = height
    },
    INITIALIZE_RENDERER (state, el) {
      // console.log(el)
      // console.log(el.offsetWidth)
      // console.log(el.offsetHeight)
      state.renderer = new WebGLRenderer({ antialias: true, preserveDrawingBuffer: true })
      // console.log(window.devicePixelRatio)
      state.renderer.setPixelRatio(window.devicePixelRatio)
      state.renderer.setSize(state.width, state.height)
      el.appendChild(state.renderer.domElement)
    },
    INITIALIZE_CAMERA (state) {
      state.camera = new PerspectiveCamera(
        // 1. Field of View (degrees)
        50,
        // 2. Aspect ratio
        state.width / state.height,
        // 3. Near clipping plane
        1,
        // 4. Far clipping plane
        1000
      )
      state.camera.position.z = 500
    },
    INITIALIZE_CONTROLS (state) {
      state.controls = new TrackballControls(
        state.camera,
        state.renderer.domElement
      )
      state.controls.rotateSpeed = 1.0
      state.controls.zoomSpeed = 1.2
      state.controls.panSpeed = 0.8
      state.controls.noZoom = false
      state.controls.noPan = false
      state.controls.staticMoving = true
      state.controls.dynamicDampingFactor = 0.3
      state.controls.keys = [65, 83, 68]
    },
    UPDATE_CONTROLS (state) {
      state.controls.update()
    },
    INITIALIZE_SCENE (state, { points, modalFile }) {
      state.scene = new Scene()
      state.scene.background = new Color(0xd9ecff)
      // state.scene.fog = new FogExp2(0xcccccc, 0.002)
      state.pyramids = []
      // START: this part is about using objloader to load 3D modal
      // var mtlLoader = new MTLLoader()
      // var objLoader = new OBJLoader()
      // mtlLoader.load('static/threeDs/girl_complete_03.mtl', function (material) {
      //   objLoader.setMaterials(material)
      //     .load('/static/threeDs/girl_complete_03.obj', function (obj) {
      //       obj.scale.set(10, 10, 10)
      //       obj.position.set(0, 0, 0)
      //       let bbox = new Box3().setFromObject(obj)
      //       // x = bbox.max.x - bbox.min.x
      //       // y = bbox.max.y - bbox.min.y
      //       // z = bbox.max.z - bbox.min.z
      //       obj.position.set(
      //         -(bbox.max.x + bbox.min.x) / 2,
      //         -(bbox.max.y + bbox.min.y) / 2,
      //         -(bbox.max.z + bbox.min.z) / 2
      //       )
      //       state.scene.add(obj)
      //     })
      // })
      // END: part END

      if (modalFile) {
        state.modalData = []
        // var objLoader = new OBJLoader()
        // var fileName = '/static/threeDs/' + modalFile + '.obj'
        // objLoader.load(fileName, function (obj) {
        //   console.log(obj)
        //   console.log(obj.children[0].material)
        //   obj.scale.set(200, 200, 200)
        //   obj.traverse(function (child) {
        //     if (child instanceof Mesh) {
        //       console.log('aaaa')
        //       child.material.transparent = true
        //     }
        //   })
        //   obj.position.set(0, 0, 0)
        //   let bbox = new Box3().setFromObject(obj)
        //   // x = bbox.max.x - bbox.min.x
        //   // y = bbox.max.y - bbox.min.y
        //   // z = bbox.max.z - bbox.min.z
        //   obj.position.set(
        //     -(bbox.max.x + bbox.min.x) / 2,
        //     -(bbox.max.y + bbox.min.y) / 2,
        //     -(bbox.max.z + bbox.min.z) / 2
        //   )
        //   obj.children[0].geometry.center()
        //   obj.children[0].material.size = 6
        //   obj.children[0].material.color.set(0xff0000)
        //   state.scene.add(obj)
        // })

        // START: this part is to load point clouds
        // var fileName = '/static/threeDs/' + modalFile + '.json'
        // var fileName = '/static/threeDs/D00001.json'
        // var request = new XMLHttpRequest()
        // request.open('get', fileName)
        // request.send(null)
        // request.onload = function () {
        //   if (request.status === 200) {
        //     var json1 = JSON.parse(request.responseText)
        //     var geometry1 = new Geometry()
        //     var material1 = new PointsMaterial({
        //       size: 1,
        //       color: 0xff0000
        //       // flatShading: true
        //       // vertexColors: true,
        //       // color: 0xffffff
        //     })
        //     // console.log(json1)
        //     // var points1 = JSON.parse(fileName)
        //     var pointset1 = json1.point_set
        //     var x1, y1, z1
        //     for (var i = 0; i < pointset1.length; i++) {
        //       x1 = pointset1[i][0] * 200
        //       y1 = pointset1[i][1] * 200
        //       z1 = pointset1[i][2] * 200
        //       var particle1 = new Vector3(x1, y1, z1)
        //       geometry1.vertices.push(particle1)
        //       // geometry.colors.push(new Color((Math.random()) * 0x00ffff))
        //     }
        //     var cloud1 = new Points(geometry1, material1)
        //     state.scene.add(cloud1)

        //     // var meshGeometry = new ConvexGeometry(geometry1.vertices)
        //     // var meshMaterial = new MeshLambertMaterial({
        //     //   color: 0xffffff,
        //     //   opacity: 0.5,
        //     //   transparent: true
        //     // })
        //     // var mesh = new Mesh(meshGeometry, meshMaterial)
        //     // state.scene.add(mesh)
        //   }
        // }

        // START: load_obj as mesh
        var objLoader = new OBJLoader()
        var fileName = '/static/threeDs/' + modalFile + '.obj'
        // var fileName = '/static/threeDs/test.obj'
        // console.log(fileName)
        objLoader.load(fileName, function (obj) {
          console.log(obj)
          console.log(obj.children[0].material)
          obj.scale.set(200, 200, 200)
          obj.traverse(function (child) {
            if (child instanceof Mesh) {
              child.material = new MeshNormalMaterial({
                // color: 0xffffff
                // transparent: true,
                // opacity: 0.2
              })
            }
          })
          obj.position.set(0, 0, 0)
          state.modalData.push(obj)
          // state.scene.add(obj)
          state.scene.add(...state.modalData)
        })
      }

      // START: this part is about point clouds
      var geometry = new Geometry()
      var material = new PointsMaterial({
        size: 2,
        // color: 0x0000ff
        // flatShading: true
        vertexColors: true
        // color: 0xffffff
      })
      points = JSON.parse(points)
      var pointset = points.point_set
      var x, y, z
      for (var j = 0; j < pointset.length; j++) {
        x = pointset[j][0] * 200
        y = pointset[j][1] * 200
        z = pointset[j][2] * 200
        var particle = new Vector3(x, y, z)
        geometry.vertices.push(particle)
        geometry.colors.push(new Color((Math.random()) * 0x00ffff))
      }
      var cloud
      cloud = new Points(geometry, material)
      state.pyramids.push(cloud)
      // state.scene.add(cloud)
      state.scene.add(...state.pyramids)
      // END: this part is about point clouds

      // START: this part is about mesh
      // var geometry1 = new CylinderBufferGeometry(0, 100, 300, 20, 1)
      // // params: up,dowm,height,mesh number,
      // var material1 = new MeshPhongMaterial({
      //   color: 0xffffff,
      //   flatShading: true
      // })
      // var mesh = new Mesh(geometry1, material1)
      // mesh.position.x = 0
      // mesh.position.y = 0
      // mesh.position.z = 0
      // mesh.updateMatrix()
      // mesh.matrixAutoUpdate = false
      // state.pyramids.push(mesh)
      // state.scene.add(...state.pyramids)
      // END: this part is about mesh

      // lights
      var lightA = new DirectionalLight(0xffffff)
      lightA.position.set(1, 1, 1)
      state.scene.add(lightA)
      var lightB = new DirectionalLight(0x002288)
      lightB.position.set(-1, -1, -1)
      state.scene.add(lightB)
      var lightC = new AmbientLight(0x222222)
      state.scene.add(lightC)

      // Axis Line 1
      var materialB = new LineBasicMaterial({ color: 0x0000ff })
      var geometryB = new Geometry()
      geometryB.vertices.push(new Vector3(0, -1000, 0))
      geometryB.vertices.push(new Vector3(0, 1000, 0))
      var lineA = new Line(geometryB, materialB)
      state.axisLines.push(lineA)

      // Axis Line 2
      var materialC = new LineBasicMaterial({ color: 0x00ff00 })
      var geometryC = new Geometry()
      geometryC.vertices.push(new Vector3(-1000, 0, 0))
      geometryC.vertices.push(new Vector3(1000, 0, 0))
      var lineB = new Line(geometryC, materialC)
      state.axisLines.push(lineB)

      // Axis 3
      var materialD = new LineBasicMaterial({ color: 0xff0000 })
      var geometryD = new Geometry()
      geometryD.vertices.push(new Vector3(0, 0, -1000))
      geometryD.vertices.push(new Vector3(0, 0, 1000))
      var lineC = new Line(geometryD, materialD)
      state.axisLines.push(lineC)

      state.scene.add(...state.axisLines)
    },
    RESIZE (state, { width, height }) {
      state.width = width
      state.height = height
      state.camera.aspect = width / height
      state.camera.updateProjectionMatrix()
      state.renderer.setSize(width, height)
      state.controls.handleResize()
      state.renderer.render(state.scene, state.camera)
    },
    SET_CAMERA_POSITION (state, { x, y, z }) {
      if (state.camera) {
        state.camera.position.set(x, y, z)
      }
    },
    RESET_CAMERA_ROTATION (state) {
      if (state.camera) {
        state.camera.rotation.set(0, 0, 0)
        state.camera.quaternion.set(0, 0, 0, 1)
        state.camera.up.set(0, 1, 0)
        state.controls.target.set(0, 0, 0)
      }
    },
    HIDE_AXIS_LINES (state) {
      state.scene.remove(...state.axisLines)
      state.renderer.render(state.scene, state.camera)
    },
    SHOW_AXIS_LINES (state) {
      state.scene.add(...state.axisLines)
      state.renderer.render(state.scene, state.camera)
    },
    HIDE_PYRAMIDS (state) {
      state.scene.remove(...state.pyramids)
      state.renderer.render(state.scene, state.camera)
    },
    SHOW_PYRAMIDS (state) {
      state.scene.add(...state.pyramids)
      state.renderer.render(state.scene, state.camera)
    },
    HIDE_MODALDATA (state) {
      state.scene.remove(...state.modalData)
      state.renderer.render(state.scene, state.camera)
    },
    SHOW_MODALDATA (state) {
      state.scene.add(...state.modalData)
      state.renderer.render(state.scene, state.camera)
    },
    GET_PNG (state) {
      // console.log('jin lai le')
      // 创建一个超链接元素，用来下载保存数据的文件
      // var link = document.createElement('a')
      // 通过超链接herf属性，设置要保存到文件中的数据
      // var canvas = state.renderer.domElement
      // console.log(canvas)
      // 获取canvas对象
      // link.href = canvas.toDataURL('image/png')
      // console.log(link.href)
      // link.download = 'threejs.png'
      // 下载文件名
      // link.click()
      // js代码触发超链接元素a的鼠标点击事件，开始下载文件到本地
      // return 'sss'
    }
  },
  actions: {
    INIT ({ state, commit }, { width, height, el, points, modalFile }) {
      return new Promise(resolve => {
        commit('SET_VIEWPORT_SIZE', { width, height })
        commit('INITIALIZE_RENDERER', el)
        commit('INITIALIZE_CAMERA')
        commit('INITIALIZE_CONTROLS')
        commit('INITIALIZE_SCENE', { points, modalFile })
        // console.log(modalFile)

        // Initial scene rendering
        state.renderer.render(state.scene, state.camera)

        // Add an event listener that will re-render
        // the scene when the controls are changed
        state.controls.addEventListener('change', () => {
          state.renderer.render(state.scene, state.camera)
        })

        resolve()
      })
    },
    ANIMATE ({ state, dispatch }) {
      window.requestAnimationFrame(() => {
        dispatch('ANIMATE')
        state.controls.update()
      })
    }
  }
})

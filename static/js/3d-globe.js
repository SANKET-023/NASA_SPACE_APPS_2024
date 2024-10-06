// 3D Rotating Globe Code (using Three.js)
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('globe-container').appendChild(renderer.domElement);

const geometry = new THREE.SphereGeometry(5, 32, 32);
const material = new THREE.MeshBasicMaterial({
    map: new THREE.TextureLoader().load('https://threejs.org/examples/textures/earth.jpg'),
});
const globe = new THREE.Mesh(geometry, material);
scene.add(globe);

camera.position.z = 10;

function animate() {
    requestAnimationFrame(animate);
    globe.rotation.y += 0.01;
    renderer.render(scene, camera);
}
animate();

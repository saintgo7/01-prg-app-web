/**
 * MobX State Tree 프로젝트
 * 기본 진입점 파일
 */

console.log('🚀 Welcome to MobX State Tree!');
console.log('=' .repeat(50));

// 여기에 코드를 작성하세요
function init() {
    console.log('✅ MobX State Tree initialized successfully');
    console.log('📦 Ready to use!');
}

init();

// 예제 기능
function exampleFeature() {
    return {
        name: 'MobX State Tree',
        version: '1.0.0',
        status: 'active'
    };
}

console.log('📊 Project Info:', exampleFeature());

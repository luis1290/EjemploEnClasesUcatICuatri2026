<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;


/*
|--------------------------------------------------------------------------
| Ruta de prueba
|--------------------------------------------------------------------------
*/

Route::get('/ping', function () {
    return response()->json([
        'message' => 'API funcionando correctamente'
    ]);
});


/*
|--------------------------------------------------------------------------
| Grupo de rutas protegidas
|--------------------------------------------------------------------------
*/

Route::middleware(['auth:sanctum'])->group(function () {

    Route::get('/perfil', function () {
        return response()->json([
            'message' => 'Ruta protegida'
        ]);
    });

});